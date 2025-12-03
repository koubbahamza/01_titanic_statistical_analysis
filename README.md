🧠 Titanic — Data Analysis & Machine Learning Pipeline
🎯 Objectif du projet

Ce projet consiste à développer une analyse exploratoire complète (EDA) ainsi qu’un pipeline de Machine Learning automatisé pour prédire la survie des passagers du Titanic dans le cadre du défi Kaggle :

👉 Titanic — Machine Learning from Disaster

Les objectifs principaux sont :

Comprendre les facteurs influençant la survie

Construire un pipeline propre, modulaire et réutilisable

Entraîner un modèle Random Forest optimisé

Générer automatiquement des fichiers de submission Kaggle

Structurer un projet comme un véritable workflow Data Science professionnel

📊 Données utilisées

Les données proviennent du concours officiel Kaggle :
🔗 https://www.kaggle.com/c/titanic/data

Variables principales :

Survived — cible (0 = mort, 1 = survécu)

Pclass — classe du billet

Sex, Age, Fare

Embarked — port d’embarquement

SibSp, Parch — famille

Cabin, Ticket, Name — features textuelles à transformer

🔧 Technologies & Librairies
🧪 Analyse & Manipulation

Python 3.13

Pandas, NumPy

Matplotlib, Seaborn

🤖 Machine Learning

Scikit-learn

RandomForestClassifier

cross_val_score

🏗 Structuration

Architecture modulaire src/

Pipeline reproductible et automatisé

Export automatique de submissions (timestamp)

Notebook dédié à l’EDA

🧱 Architecture du projet
01_titanic_statistical_analysis/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── submission/
│       ├── submission_random_forest.csv
│       └── submission_random_forest_2025xxxx_xxxxxx.csv
│
├── notebooks/
│   └── 01_data_analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── model_random_forest.py
│   └── train_pipeline.py
│
├── requirements.txt
├── README.md
└── .gitignore

🧩 Pipeline Machine Learning

Le pipeline (défini dans train_pipeline.py) suit les étapes suivantes :

1️⃣ Chargement des données

train / test

concaténation en dataset global pour le preprocessing

2️⃣ Feature Engineering

Création de variables dérivées :

Title (extrait du nom)

Deck (extrait du Cabin)

FamilySize

FarePerPerson

Age*Class (interaction)

3️⃣ Imputation intelligente

Age → médiane par Title

Fare → médiane

Embarked → mode

4️⃣ Nettoyage

Suppression des colonnes non exploitables :
Name, Ticket, Cabin

5️⃣ Encodage

One-Hot Encoding global

Alignement train/test garanti

6️⃣ Entraînement du modèle

Modèle : RandomForestClassifier

Hyperparamètres optimisés

Cross-validation 5-fold

7️⃣ Génération de la submission

Prédiction sur X_test

Export automatique :

data/submission/submission_random_forest_YYYYMMDD_HHMMSS.csv

📊 Résultats du modèle
Cross-validation (5 folds) :
Scores = [0.82, 0.82, 0.83, 0.81, 0.85]
Score moyen = 0.827


Ces résultats sont cohérents avec les meilleurs benchmarks Random Forest sur Titanic.

🚀 Comment exécuter le pipeline
1) Activer l’environnement virtuel
.\.venv\Scripts\activate

2) Lancer le pipeline complet
python src/train_pipeline.py

3) Résultat

Un fichier de submission Kaggle est généré automatiquement dans :

data/submission/

📒 Notebook d’analyse

Le notebook 01_data_analysis.ipynb contient :

Analyse exploratoire complète

Visualisations et corrélations

Tests de modèles

Cross-validation

Interprétations

Il sert de zone d’expérimentation, tandis que src/ contient la logique industrialisée.

💡 Compétences développées

Structuration d’un projet ML complet

Feature engineering avancé

Traitement des valeurs manquantes

Encodage cohérent train/test

Cross-validation

Production de pipelines automatisés

Génération de fichiers de submission

Industrialisation et nettoyage du code

👤 Auteur

Hamza Koubba
Data Scientist & IoT Engineer — Industrie 4.0 • IA & R&D

📧 hamzakoubba95@gmail.com

🔗 LinkedIn : https://www.linkedin.com/in/koubba/