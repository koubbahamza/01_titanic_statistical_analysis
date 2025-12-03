🧠 Titanic — Data Analysis & Machine Learning Pipeline
🎯 Objectif du projet

Ce projet consiste à développer une analyse exploratoire complète (EDA) et un pipeline de Machine Learning entièrement automatisé pour résoudre le célèbre défi Kaggle :
👉 Titanic — Machine Learning from Disaster.

L’objectif est de :

comprendre les facteurs influençant la survie

construire un pipeline propre, modulaire, réutilisable

entraîner un modèle Random Forest optimisé

générer automatiquement des fichiers de submission Kaggle

structurer le projet comme un véritable projet Data Science professionnel

📊 Données utilisées

Les données proviennent du concours officiel Kaggle :
🔗 https://www.kaggle.com/c/titanic/data

Variables principales :

Survived — cible (0 = mort, 1 = survécu)

Pclass — classe du billet (1ère à 3e)

Sex — sexe

Age — âge

Fare — prix du billet

Embarked — port d’embarquement

SibSp, Parch — famille

Cabin, Ticket, Name — textes à transformer

🔧 Technologies & Librairies
🧪 Analyse & Manipulation

Python 3.13

Pandas, NumPy

Seaborn, Matplotlib

🤖 Machine Learning

Scikit-learn

RandomForestClassifier

cross_val_score

🏗 Structuration du projet

Architecture modulaire src/

Pipeline reproductible

Génération automatique des CSV avec timestamp

Notebook pour l’EDA et les tests de modèles

🧱 Architecture du projet
01_titanic_statistical_analysis/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   ├── submission/
│   │   ├── submission_random_forest.csv
│   │   └── submission_random_forest_2025xxxx_xxxxxx.csv
│
├── notebooks/
│   └── 01_data_analysis.ipynb          # EDA complète + tests modèles
│
├── src/
│   ├── preprocessing.py                 # Feature engineering, imputation, encoding
│   ├── model_random_forest.py           # Entraînement RF modulaire
│   └── train_pipeline.py                # Pipeline ML complet (automatisé)
│
├── requirements.txt
├── README.md
└── .gitignore

🧩 Pipeline Machine Learning

Le pipeline complet (défini dans train_pipeline.py) suit les étapes :

1️⃣ Chargement des données

train / test

concaténation dans full

2️⃣ Feature Engineering

Création des variables clés :

Title (extrait du nom)

Deck (extrait de Cabin)

FamilySize

FarePerPerson

Age*Class

3️⃣ Imputation intelligente

Age → médiane par Title

Fare → médiane

Embarked → mode

4️⃣ Nettoyage des colonnes inutiles

Suppression de : Name, Ticket, Cabin

5️⃣ One-Hot Encoding global

Sur : Sex, Embarked, Title, Deck

6️⃣ Séparation train/test alignée

Garantie que les colonnes sont strictement identiques.

7️⃣ Entraînement modèle

RandomForestClassifier

Hyperparamètres optimisés (n_estimators, max_depth, etc.)

Cross-validation (5 folds)

8️⃣ Génération de la submission

Predictions sur X_test

CSV exporté automatiquement dans data/submission/

Nom unique avec timestamp

🧪 Résultats du modèle

Cross-validation (5 folds) :

Scores = [0.82, 0.82, 0.83, 0.81, 0.85]
Score moyen = ~0.827


Le modèle Random Forest donne des performances stables et cohérentes avec les benchmarks connus du Titanic.

🚀 Comment exécuter le pipeline
1) Activer l’environnement virtuel
.\.venv\Scripts\activate

2) Lancer le pipeline complet
python src/train_pipeline.py

3) Résultat

Un fichier est généré automatiquement :

data/submission/submission_random_forest_YYYYMMDD_HHMMSS.csv


➡️ Il peut être déposé directement sur Kaggle.

📒 Notebook d'analyse

Le notebook notebooks/01_data_analysis.ipynb contient :

EDA complète

visualisations

corrélations

test de modèles

validation croisée

interprétations

Ce notebook sert d’espace d’analyse, tandis que src/ contient le pipeline propre en production.

💡 Compétences développées

Structuration d’un projet ML complet

Feature engineering avancé

Traitement des valeurs manquantes

One-Hot encoding cohérent entre train/test

Cross-validation

Gestion d’un pipeline automatisé

Génération de fichiers de submission

Nettoyage & industrialisation du code

👤 Auteur

Hamza Koubba
Data Scientist & IoT Engineer • Industrie 4.0 • IA & R&D

📧 hamzakoubba95@gmail.com

🔗 LinkedIn : https://www.linkedin.com/in/koubba/