-- AI Academy • Supabase SQL Editor • exécuter une seule fois sur un NOUVEAU projet
-- Auth email/mot de passe via Supabase Auth.
create extension if not exists pgcrypto;
create schema if not exists private;

create table public.profiles (
  user_id uuid primary key references auth.users(id) on delete cascade,
  display_name text not null default 'Étudiant',
  created_at timestamptz not null default now(),
  constraint name_length check (char_length(display_name) between 1 and 60)
);
create table public.study_groups (
  id uuid primary key default gen_random_uuid(),
  invite_code text unique not null default upper(encode(gen_random_bytes(8),'hex')),
  owner_id uuid not null references auth.users(id),
  created_at timestamptz not null default now()
);
create table public.group_members (
  user_id uuid primary key references auth.users(id) on delete cascade,
  group_id uuid not null references public.study_groups(id) on delete cascade,
  joined_at timestamptz not null default now()
);
create index members_group_idx on public.group_members(group_id);
create table public.lesson_progress (
  user_id uuid not null references auth.users(id) on delete cascade,
  lesson_id text not null,
  completed boolean not null default false,
  updated_at timestamptz not null default now(),
  primary key(user_id,lesson_id),
  constraint valid_lesson_id check (lesson_id ~ '^m(0?[1-9]|1[0-5])-w[1-4]-d[1-5]$')
);
create table public.study_notes (
  id uuid primary key default gen_random_uuid(),
  author_id uuid not null references auth.users(id) on delete cascade,
  lesson_id text,
  title text not null,
  content text not null,
  shared boolean not null default false,
  updated_at timestamptz not null default now(),
  constraint note_title_length check (char_length(title) between 1 and 150),
  constraint note_body_length check (char_length(content) between 1 and 20000)
);
create index notes_author_idx on public.study_notes(author_id);
create table public.evaluations (
  user_id uuid not null references auth.users(id) on delete cascade,
  week_id text not null,
  score integer not null check (score between 0 and 20),
  feedback text not null default '',
  updated_at timestamptz not null default now(),
  primary key(user_id,week_id),
  constraint valid_week_id check (week_id ~ '^m(0?[1-9]|1[0-5])-w[1-4]$')
);

-- Groupe commun, mais chaque membre garde ses propres données.
-- SECURITY DEFINER seulement pour les fonctions contrôlées ci-dessous.
create or replace function private.is_teammate(other uuid)
returns boolean language sql stable security definer set search_path = '' as $$
  select other = (select auth.uid()) or exists (
    select 1 from public.group_members mine
    join public.group_members theirs on theirs.group_id = mine.group_id
    where mine.user_id = (select auth.uid()) and theirs.user_id = other
  );
$$;
revoke all on function private.is_teammate(uuid) from public;
grant usage on schema private to authenticated;
grant execute on function private.is_teammate(uuid) to authenticated;

create or replace function public.create_duo()
returns text language plpgsql security definer set search_path = '' as $$
declare uid uuid := (select auth.uid()); g uuid; code text;
begin
  if uid is null then raise exception 'Connexion requise'; end if;
  if exists(select 1 from public.group_members where user_id=uid) then raise exception 'Tu appartiens déjà à un duo'; end if;
  insert into public.study_groups(owner_id) values(uid) returning id,invite_code into g,code;
  insert into public.group_members(user_id,group_id) values(uid,g);
  return code;
end;$$;
create or replace function public.join_duo(p_code text)
returns void language plpgsql security definer set search_path = '' as $$
declare uid uuid := (select auth.uid()); g uuid; n integer;
begin
  if uid is null then raise exception 'Connexion requise'; end if;
  if exists(select 1 from public.group_members where user_id=uid) then raise exception 'Tu appartiens déjà à un duo'; end if;
  select id into g from public.study_groups where invite_code=upper(trim(p_code)) for update;
  if g is null then raise exception 'Code d’invitation incorrect'; end if;
  select count(*) into n from public.group_members where group_id=g;
  if n >= 2 then raise exception 'Ce duo contient déjà deux personnes'; end if;
  insert into public.group_members(user_id,group_id) values(uid,g);
end;$$;
revoke all on function public.create_duo() from public,anon;
revoke all on function public.join_duo(text) from public,anon;
grant execute on function public.create_duo() to authenticated;
grant execute on function public.join_duo(text) to authenticated;

alter table public.profiles enable row level security;
alter table public.study_groups enable row level security;
alter table public.group_members enable row level security;
alter table public.lesson_progress enable row level security;
alter table public.study_notes enable row level security;
alter table public.evaluations enable row level security;

create policy profiles_read on public.profiles for select to authenticated using (private.is_teammate(user_id));
create policy profiles_write on public.profiles for insert to authenticated with check (user_id=(select auth.uid()));
create policy profiles_update on public.profiles for update to authenticated using(user_id=(select auth.uid())) with check(user_id=(select auth.uid()));
create policy groups_read on public.study_groups for select to authenticated using(exists(select 1 from public.group_members where group_id=id and user_id=(select auth.uid())));
create policy members_read on public.group_members for select to authenticated using(private.is_teammate(user_id));
create policy progress_read on public.lesson_progress for select to authenticated using(private.is_teammate(user_id));
create policy progress_insert on public.lesson_progress for insert to authenticated with check(user_id=(select auth.uid()));
create policy progress_update on public.lesson_progress for update to authenticated using(user_id=(select auth.uid())) with check(user_id=(select auth.uid()));
create policy notes_read on public.study_notes for select to authenticated using(author_id=(select auth.uid()) or (shared and private.is_teammate(author_id)));
create policy notes_insert on public.study_notes for insert to authenticated with check(author_id=(select auth.uid()));
create policy notes_update on public.study_notes for update to authenticated using(author_id=(select auth.uid())) with check(author_id=(select auth.uid()));
create policy notes_delete on public.study_notes for delete to authenticated using(author_id=(select auth.uid()));
create policy evaluations_read on public.evaluations for select to authenticated using(private.is_teammate(user_id));
create policy evaluations_insert on public.evaluations for insert to authenticated with check(user_id=(select auth.uid()));
create policy evaluations_update on public.evaluations for update to authenticated using(user_id=(select auth.uid())) with check(user_id=(select auth.uid()));

revoke all on public.profiles,public.study_groups,public.group_members,public.lesson_progress,public.study_notes,public.evaluations from anon;
grant select,insert,update on public.profiles to authenticated;
grant select on public.study_groups,public.group_members to authenticated;
grant select,insert,update on public.lesson_progress to authenticated;
grant select,insert,update,delete on public.study_notes to authenticated;
grant select,insert,update on public.evaluations to authenticated;
-- Limite d'accès : aucun client ne peut écrire pour un autre compte;
-- les notes non partagées sont invisibles au partenaire, y compris via l'API.
