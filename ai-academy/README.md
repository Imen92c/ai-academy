# ✳ AI Academy — formation IA en duo

Une première version de plateforme de formation IA en français, avec **15 mois, 60 semaines, 300 leçons et 300 exercices**, tableau de bord, progression individuelle/partagée, notes privées/partagées et évaluations sur 20.

## 1. Tester tout de suite (sans compte)

Les fichiers doivent être servis en HTTP pour charger `curriculum.json`.

**Avec VS Code :** ouvre le dossier `ai-academy` puis lance **Live Server** sur `index.html` (si l'extension est installée).

**Ou avec Python**, dans le dossier :

```powershell
python -m http.server 5500
```

Puis ouvre `http://localhost:5500`.

Sans configuration Supabase, l'application s'ouvre automatiquement en **mode démonstration**, avec deux utilisateurs fictifs interchangeables via le menu en bas à gauche. Les données sont alors sauvegardées **uniquement dans le navigateur de cet appareil**. Le mode démonstration ne synchronise pas deux vrais utilisateurs.

## 2. Activer les vrais comptes et la synchronisation (Supabase)

1. Crée un projet gratuit sur https://supabase.com/dashboard.
2. Ouvre **SQL Editor** dans ce projet.
3. Colle le contenu de `schema.sql` et exécute-le (dans un projet neuf, une seule fois).
4. Dans **Authentication → Providers → Email**, garde l'authentification e-mail activée. Pour un vrai site accessible en ligne, conserve la confirmation par e-mail activée.
5. Dans **Project Settings → API Keys** (intitulé pouvant évoluer), récupère la **Project URL** et la **Publishable key**. Une ancienne **anon key** fonctionne aussi.
6. Ouvre `config.js` et remplis :

```js
window.AI_ACADEMY_CONFIG = {
  supabaseUrl: 'https://TON-PROJET.supabase.co',
  supabasePublishableKey: 'TA_CLE_PUBLISHABLE'
};
```

7. Dans **Authentication → URL Configuration**, définis l'URL officielle de ton site une fois publié, ainsi que les **Redirect URLs** utiles pour le développement (`http://localhost:5500/**`, URL GitHub Pages, etc.).
8. Recharge le site : un formulaire de connexion et d'inscription apparaît. Chacun crée son compte avec une **adresse e-mail différente**.
9. Une fois connectée, ouvre **Notre binôme → Créer notre duo**. Copie le code d'invitation et transmets-le à ton ami. Il se connecte et choisit **Rejoindre mon ami** avec ce code.

**Important :** Ne colle **jamais** une clé `service_role`, `sb_secret_...` ou ton mot de passe dans `config.js` / GitHub. La clé publishable est destinée au navigateur. Les données sont protégées par des politiques Row Level Security (RLS) dans `schema.sql`.

## 3. Héberger gratuitement sur GitHub Pages

1. Crée un dépôt GitHub (par exemple `ai-academy`).
2. Copie dans ce dépôt : `index.html`, `style.css`, `app.js`, `config.js`, `curriculum.json` (et facultativement `README.md` et `schema.sql`).
3. Depuis le terminal du dossier :

```powershell
git init
git add .
git commit -m "Première version AI Academy"
git branch -M main
git remote add origin https://github.com/TON-PSEUDO/ai-academy.git
git push -u origin main
```

Si le dépôt existe déjà et possède `origin`, **ne réutilise pas** `git remote add origin` ; vérifie `git remote -v`.

4. Sur GitHub, ouvre **Settings → Pages**. Dans **Build and deployment**, choisis **Deploy from a branch**, puis `main` et `/ (root)`, et enregistre.
5. Après publication, le lien ressemblera à `https://TON-PSEUDO.github.io/ai-academy/`.
6. Ajoute **cette URL exacte** aux Redirect URLs Supabase. Partage le lien GitHub Pages à ton ami. Vous pourrez vous connecter séparément.

> GitHub Pages héberge **uniquement le front-end statique**. Supabase héberge les comptes, les notes, les évaluations et la progression commune. GitHub Pages seul ne permettrait pas le suivi entre deux PC.

## 4. Organisation des fichiers

- `index.html` — structure de l'interface et écran d'authentification
- `style.css` — design responsive
- `app.js` — logique, progression, notes, quiz et connexion Supabase
- `curriculum.json` — **15 mois × 4 semaines × 5 jours** avec exercice quotidien
- `config.js` — **tes identifiants publics** Supabase (à remplir)
- `schema.sql` — tables PostgreSQL, fonctions de groupe, permissions RLS
- `build_curriculum.py` — source utilisée pour construire les leçons JSON (optionnelle pour le déploiement)

## 5. Règles du partage

- Chaque utilisateur marque **uniquement ses propres leçons**.
- Chacun voit la progression globale et les contrôles de son binôme.
- Une note est **privée par défaut** : seul son auteur peut y accéder.
- L'auteur peut cocher **Partager** : l'autre peut lire, pas modifier ni supprimer.
- Un groupe est limité à **deux personnes**, avec un code d'invitation de 16 caractères hexadécimaux généré aléatoirement.
- Les comptes individuels sont gérés par Supabase Auth.

## 6. Périmètre de cette première version

**Inclus :** parcours détaillé, exercice par jour, suivi, notes, partage, évaluations manuelles sur 20, interface mobile, mode démo et synchronisation cloud une fois Supabase configuré.

**Pas encore inclus :** correction automatique des exercices, éditeur de code intégré, messagerie temps réel, remise de fichiers, statistiques très avancées et contenus complets rédigés de chaque leçon. Les intitulés et exercices sont prêts ; les cours détaillés peuvent être ajoutés progressivement.

## 7. Points de vigilance

- Les notes textuelles et scores sont sauvegardés dans Supabase si configuré ; en mode démo, un effacement de stockage navigateur les fait disparaître.
- Les accès sont bornés par les politiques RLS. Testez avec **deux vrais comptes** avant de partager des notes sensibles.
- Évite de mettre des secrets dans les notes ou dans le dépôt public GitHub.
- Ce projet est une base pédagogique ; les contrôles, la sécurité, l'accessibilité et la qualité doivent être réévalués avant un usage à grande échelle.
