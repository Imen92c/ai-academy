import json
from pathlib import Path
# Each week: title; 5 distinct lesson:exercise combinations.
raw = '''Fondamentaux & Python
Ordinateur et matériel;CPU et processeur:Schématise les étapes d'exécution d'une application;RAM et stockage:Compare RAM SSD et HDD en cinq phrases;Logiciels et OS:Classe quinze exemples en système ou application;Fichiers et dossiers:Crée une arborescence organisée avec dix fichiers;Terminal et Git:Initialise un dépôt et réalise deux commits
Logique informatique;Binaire:Convertis dix nombres de base dix en binaire;Bits et octets:Calcule le poids de cinq fichiers fictifs;Booléens:Établis trois tables de vérité;Pseudocode:Écris les étapes d'un distributeur de tickets;Organigrammes:Dessine un algorithme de vérification d'âge
Python premières lignes;Installer Python:Lance un script depuis le terminal;Print et commentaires:Affiche ta fiche personnelle sur cinq lignes;Variables:Crée douze variables correctement nommées;Opérateurs:Programme une calculatrice simple;Entrée utilisateur:Crée un convertisseur Celsius Fahrenheit
Conditions et boucles;Conditions if:Applique une réduction selon l'âge;Comparateurs:Trouve le maximum de trois nombres;Boucle for:Affiche les dix tables de multiplication;Boucle while:Crée un jeu de devinette;Projet du mois:Construis un menu de calculatrice et explique ton code
Python approfondi
Collections;Listes:Crée une liste de courses modifiable;Tuples et sets:Supprime les doublons de prénoms;Dictionnaires:Construis un carnet de contacts;Itération:Calcule les moyennes d'une classe;Mini-projet:Programme un inventaire en mémoire
Fonctions;def et return:Transforme trois exercices en fonctions;Arguments:Construis un calculateur de TVA;Portée:Corrige quatre erreurs de portée;Modules:Divise un programme en trois fichiers;Mini-projet:Crée une boîte à outils Python
Fichiers et robustesse;Lire et écrire:Enregistre un journal texte;JSON et CSV:Exporte dix données puis réimporte-les;Exceptions:Traite cinq saisies incorrectes;pathlib:Organise des fichiers dans un dossier de test;Mini-projet:Sauvegarde une todo-list dans un JSON
POO et tests;Classes:Crée une classe Produit;Objets et composition:Code un panier avec plusieurs produits;pip et venv:Crée un environnement propre;pytest:Écris six tests unitaires;Examen:Conçois un gestionnaire de réservations
Algorithmique, maths et SQL
Maths de base;Fractions et pourcentages:Résous dix calculs de promotions;Équations:Résous cinq équations du premier degré;Fonctions:Trace trois fonctions;Logique en maths:Travaille les ensembles et intersections;Projet:Simule des intérêts composés
Recherche et tri;Recherche linéaire:Programme ta propre fonction de recherche;Recherche binaire:Recherche dans une liste triée;Tri par sélection:Code le tri sans sort;Complexité:Compte les opérations des algorithmes;Mini-projet:Compare les temps de recherche
Structures de données;Pile:Crée un historique annuler;File:Simule une file d'attente;Récursivité:Écris une factorielle récursive;Graphes:Représente les connexions de six villes;Évaluation:Résous cinq problèmes sans regarder le cours
SQL;Tables:Modélise une bibliothèque;SELECT et WHERE:Écris quinze requêtes SQL;INSERT UPDATE DELETE:Gère un catalogue SQLite;JOIN et GROUP BY:Analyse les ventes de deux tables;Projet:Connecte Python à SQLite
Data science et statistiques
NumPy;ndarray:Crée trois tableaux;Indexation:Extrais dix tranches de matrices;Vectorisation:Réécris cinq boucles;Calcul matriciel:Multiplie trois matrices compatibles;Mini-projet:Normalise un jeu de données
Pandas;DataFrame:Importe et inspecte un CSV;Filtrage:Résous dix questions de données;Valeurs manquantes:Nettoie un CSV incomplet;Groupby et merge:Analyse les ventes jointes de deux fichiers;Mini-projet:Produis une exploration de données
Statistiques descriptives;Moyenne et médiane:Analyse dix échantillons;Écart-type:Vérifie des calculs à la main et dans Python;Quantiles:Détecte les valeurs extrêmes;Corrélation:Compare trois paires de variables;Mini-projet:Rédige une analyse statistique
Visualisation;Matplotlib:Crée quatre types de graphiques;Choix du visuel:Choisis le bon graphique pour cinq scénarios;Nettoyage avancé:Traite des données bruitées;Interprétation:Rédige cinq conclusions prudentes;Examen Data:Publie un notebook explicatif
Maths pour le ML
Probabilités;Événements:Résous dix exercices de tirage;Conditionnelles:Calcule cinq probabilités conditionnelles;Bayes:Analyse un test de dépistage fictif;Monte Carlo:Simule 10000 lancers;Projet:Compare probabilités théoriques et observées
Algèbre linéaire;Vecteurs:Calcule les normes de cinq vecteurs;Matrices:Additionne et multiplie des matrices;Produit scalaire:Compare des vecteurs;Transformations:Trace des points transformés;Mini-projet:Calcule la similarité cosinus
Calcul différentiel;Pentes:Mesure des pentes sur trois fonctions;Dérivées:Compare dérivées exactes et numériques;Gradient:Calcule un gradient simple;Descente de gradient:Optimise une fonction quadratique;Projet:Trace la trajectoire de convergence
Maths appliquées;Dimensions de matrices:Vérifie quinze opérations;Probabilités et classifieurs:Simule un score probabiliste;Fonction de perte:Trace MSE et MAE;Optimisation:Compare différents pas d'apprentissage;Examen:Code une petite régression linéaire
Machine Learning fondamentaux
Introduction au ML;Types de ML:Classe quinze cas d'usage;Variables features:Identifie la cible d'un dataset;Séparation des données:Crée train et test;Baseline:Construit une prédiction de référence;Projet:Entraîne un premier modèle de prix
Régression;Modèle linéaire:Entraîne une régression;Métriques:Calcule MAE MSE RMSE;Résidus:Analyse des prédictions incorrectes;Régularisation:Compare deux versions d'un modèle;Projet:Documente un prédicteur immobilier
Classification;Régression logistique:Entraîne un classifieur binaire;Arbres:Compare arbre et modèle linéaire;Confusion:Construis une matrice de confusion;F1 et recall:Choisis une métrique adaptée;Projet:Détecte des messages spam
Validation ML;Surapprentissage:Trace train vs test;Validation croisée:Teste cinq plis;Hyperparamètres:Compare cinq configurations;Pipelines:Préviens les fuites de données;Examen:Recrée un pipeline reproductible
ML intermédiaire
Prétraitement;Imputation:Compare trois traitements de valeurs manquantes;Encodage:Applique OneHotEncoder;Standardisation:Observe un changement de performance;Déséquilibre de classes:Compare les métriques;Projet:Nettoie un jeu de données réaliste
Modèles avancés;Random Forest:Compare forêt et arbre;Gradient Boosting:Teste un modèle de boosting;Sélection des variables:Retire des variables inutiles;Optimisation des paramètres:Exécute une recherche aléatoire;Projet:Présente un benchmark de trois modèles
Explicabilité;Importance:Classe dix features;Permutation:Mesure l'importance par permutation;SHAP:Explique cinq prédictions;Biais:Identifie des données insuffisantes;Projet:Rédige une fiche d'explicabilité
Projet ML complet;Définition du problème:Rédige objectif et métriques;EDA:Explore et nettoie ton dataset;Modélisation:Entraîne trois modèles;Rapport:Explique les résultats et leurs limites;Examen:Publie un projet ML complet sur GitHub
Deep Learning et PyTorch
Bases neuronales;Neurone:Calcule la sortie d'un neurone;Activations:Compare ReLU et sigmoid;Loss:Trace des erreurs de prédiction;Gradient:Explique la rétropropagation;Projet:Code un neurone avec NumPy
PyTorch;Tensors:Manipule vingt tenseurs;Shapes et device:Teste les formes CPU et GPU;Autograd:Calcule cinq gradients;nn.Module:Construis un MLP;Mini-projet:Classe un dataset tabulaire
Entraînement;Dataset DataLoader:Charge des lots;Optimizers:Compare Adam et SGD;Train validation:Écris deux boucles;Checkpoints:Sauvegarde et recharge les poids;Projet:Entraîne un modèle reproductible
Apprentissage profond pratique;Images:Entraîne un modèle de classification;Régularisation:Compare le dropout;Courbes:Repère l'overfitting;Erreurs:Analyse vingt cas ratés;Examen:Publie un réseau neuronal expliqué
Deep Learning appliqué
Vision;Convolution:Visualise trois filtres;CNN:Construis un modèle convolutionnel;Augmentation:Essaie quatre transformations;Transfer learning:Adapte un modèle pré-entraîné;Projet:Crée un classifieur d'images
Texte;Nettoyage:Prépare un corpus;Tokenisation:Compare des tokenizers simples;Vectorisation:Encode des phrases;Classification NLP:Prédit un sentiment;Projet:Analyse cinquante avis
Performance;Batch:Compare trois tailles de lots;Learning rate:Teste plusieurs taux;Mémoire GPU:Mesure temps et mémoire;Reproductibilité:Fixe les graines aléatoires;Projet:Documente cinq expériences
Projet DL;Cahier des charges:Délimite un problème de Deep Learning;Dataset:Sépare train validation et test;Training:Teste plusieurs architectures;Évaluation:Mesure les erreurs du modèle;Livrable:Publie une démonstration
Transformers et NLP
Architectures Transformer;Tokens:Tokenise quinze phrases;Embeddings:Compare la proximité de phrases;Attention:Calcule un exemple miniature;Encodeurs et décodeurs:Dessine les flux d'information;Contrôle:Explique un Transformer de mémoire
Hugging Face;Model Hub:Choisis trois modèles pertinents;Pipelines:Teste classification et génération;Tokenizers:Mesure les longueurs;Inférence:Mesure vitesse et qualité;Projet:Crée une mini-application NLP
Fine-tuning;Datasets:Étiquette un petit jeu d'exemples;Métriques:Mesure F1 et accuracy;Adapter un modèle:Effectue une expérience de fine-tuning léger;Évaluation:Compare avant et après;Projet:Documente les limites et coûts
Projet NLP;Cas d'usage:Prépare vingt cas représentatifs;Pipeline:Assemble prétraitement et modèle;Interface:Construis une page simple;Évaluation:Analyse vingt prédictions;Examen:Publie une application NLP
LLM et développement IA
LLM fondamentaux;Pré-entraînement:Compare inférence et entraînement;Contexte:Analyse une fenêtre de contexte;Paramètres de génération:Compare plusieurs sorties;Hallucinations:Prépare dix questions pièges;Projet:Crée une grille d'évaluation
APIs et SDK;HTTP JSON:Appelle une API publique de test;Client Python:Crée un client de modèle;Secrets:Stocke les clés hors du code;Erreurs:Simule une panne réseau;Projet:Développe un service de résumé
Sorties structurées;Prompt design:Compare dix consignes;Extraction JSON:Extrais les champs d'un formulaire fictif;Pydantic:Valide des réponses;Tests de prompts:Crée vingt tests;Mini-projet:Développe un extracteur de données
Application LLM;Fonctionnalités:Définis le besoin et les limites;Backend:Crée les fonctions de traitement;Interface:Construis une interface de test;Évaluation:Mesure latence et erreurs;Examen:Publie un prototype LLM
Embeddings et RAG
Recherche sémantique;Vectorisation:Calcule vingt embeddings;Similarité:Compare les distances cosinus;Top-k:Retourne cinq extraits pertinents;Indexation:Teste un index vectoriel local;Projet:Crée un moteur de recherche documentaire
Pipeline RAG;Ingestion:Lis dix documents de test;Découpage:Compare trois tailles de chunks;Retrieval:Récupère des passages pertinents;Génération:Conçois une réponse avec sources;Projet:Crée un assistant documentaire
RAG amélioré;Recherche hybride:Compare lexical et sémantique;Reranking:Réordonne les passages;Citations:Affiche des extraits justificatifs;Refus:Teste des questions sans réponse;Projet:Réduis les hallucinations
Évaluation RAG;Jeu de tests:Écris trente questions;Recall de recherche:Mesure les extraits retrouvés;Qualité:Réalise un audit manuel;Performance:Compare coût et délai;Examen:Publie un RAG testé
Agents IA
Tool calling;Agents vs workflows:Compare cinq scénarios;Schémas d'outils:Définis des arguments validés;Calculatrice:Expose un outil mathématique;Lecture de fichiers:Protège le dossier accessible;Projet:Construis un agent à trois outils
Orchestration;États:Modélise quatre étapes;smolagents:Teste un agent encadré;LangGraph:Implémente un flux simple;Gestion d'erreurs:Simule des pannes d'outils;Projet:Compare agent et workflow déterministe
Agent documentaire;Sous-tâches:Décompose une question;Recherche:Connecte un outil RAG;Sélection d'outils:Analyse les décisions;Références:Contrôle les citations;Projet:Construis un assistant multi-outils
Sécurité agents;Injection de prompt:Teste une instruction hostile fictive;Permissions:Interdis des actions risquées;Human in the loop:Ajoute une validation avant une action;Logs:Trace les appels;Examen:Effectue vingt tests de sécurité
Backend et production
FastAPI;Routes:Crée cinq endpoints;Pydantic:Valide des corps de requêtes;CRUD:Construis une API simple;Endpoint IA:Intègre une prédiction;Projet:Teste un backend IA
Docker;Images:Inspecte un conteneur;Dockerfile:Conteneurise FastAPI;Volumes:Conserve les fichiers utiles;Compose:Lance une API et une base;Projet:Démarre une application avec une commande
Tests et CI;Tests unitaires:Écris dix tests;Intégration:Teste quatre routes;GitHub Actions:Automatise les tests;Logs:Enregistre les erreurs;Projet:Livraison continue d'un dépôt
Déploiement;Cloud:Dessine une architecture;Secrets:Vérifie les variables sensibles;Hébergement:Déploie une démo;Surveillance:Teste les erreurs;Examen:Fais tester la démo par une autre personne
Projet final et portfolio
Conception finale;Sujet:Choisis un problème utile;Cahier des charges:Définis les utilisateurs;Architecture:Dessine les composants;Planning:Ouvre des issues GitHub;Livrable:Présente un dossier de conception
Construction finale;Backend:Programme une fonctionnalité de bout en bout;Données:Relie le stockage;IA:Intègre une méthode ML ou RAG;Interface:Construis le parcours principal;Livrable:Présente ton MVP
Qualité finale;Tests fonctionnels:Écris vingt scénarios;Évaluation IA:Mesure le résultat;Sécurité:Vérifie les accès;Déploiement:Mets le système en ligne;Livrable:Présente une démonstration
Portfolio et entretiens;GitHub:Signe quatre README de qualité;CV:Décris trois projets honnêtement;Python SQL:Résous dix questions techniques;IA:Explique ML RAG et embeddings;Examen final:Construis une fonctionnalité autonome'''
months=[]
for rawmonth in raw.split('\n'):
    if not rawmonth.strip(): continue
    if ';' not in rawmonth:
        months.append({'title':rawmonth,'weeks':[]});continue
    items=rawmonth.split(';')
    assert len(items)==6, (rawmonth,len(items))
    days=[]
    for t in items[1:]:
        title,ex=t.split(':',1)
        days.append({'title':title,'exercise':ex})
    months[-1]['weeks'].append({'title':items[0],'days':days})
assert len(months)==15 and all(len(m['weeks'])==4 for m in months)
assert sum(len(w['days']) for m in months for w in m['weeks'])==300
out=Path('/mnt/data/ai-academy/curriculum.json')
out.write_text(json.dumps(months,ensure_ascii=False,indent=2),encoding='utf-8')
print('Created 15 months, 60 weeks, 300 lessons')
