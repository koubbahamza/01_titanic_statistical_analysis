🧠 Titanic — Data Analysis & Machine Learning Pipeline
<div align="center">










</div>
🎯 Objectif du projet

Ce projet met en place :

une analyse exploratoire complète (EDA)

un pipeline Machine Learning automatisé

un modèle Random Forest optimisé

une génération automatique de submissions Kaggle

une architecture pro, modulaire, maintenable

Le but est de reproduire un vrai workflow Data Science professionnel, du nettoyage des données jusqu’à la production.

📊 Données utilisées

Dataset :
🔗 https://www.kaggle.com/c/titanic/data

Variables principales :

Survived (0/1)

Pclass, Sex, Age, Fare

Embarked

SibSp, Parch

Cabin, Ticket, Name (features textuelles à traiter)

🔧 Technologies & Librairies
🧪 Analyse

Python 3.13

Pandas, NumPy

Seaborn, Matplotlib

🤖 Machine Learning

Scikit-learn

RandomForestClassifier

Cross-validation

🏗 Structuration & Production

Architecture modulaire src/

Pipeline automatisé

Export CSV avec timestamp

Notebook séparé pour l’EDA

🧱 Architecture du projet
01_titanic_statistical_analysis/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── submission/
│       ├── submission_random_forest.csv
│       └── submission_random_forest_YYYYMMDD_HHMMSS.csv
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
1️⃣ Chargement des données

Import train/test

Concaténation pour preprocessing global

2️⃣ Feature Engineering

Title → extrait du champ Name

Deck → extrait de la cabine

FamilySize

FarePerPerson

Age*Class

3️⃣ Imputation

Age → médiane par Title

Fare → médiane

Embarked → mode

4️⃣ Nettoyage

Suppression :
Name, Ticket, Cabin

5️⃣ Encodage

One-Hot Encoding

Alignement strict train/test

6️⃣ Entraînement

Modèle : RandomForestClassifier

Hyperparamètres optimisés

Cross-validation (5 folds)

7️⃣ Génération de la submission

Export automatique :

data/submission/submission_random_forest_YYYYMMDD_HHMMSS.csv

📊 Résultats du modèle
Cross-validation (5 folds)
Scores = [0.82, 0.82, 0.83, 0.81, 0.85]
Score moyen = 0.827


Le Random Forest obtient des performances stables et proches des benchmarks Kaggle.

🚀 Comment exécuter le pipeline
1) Activer l’environnement virtuel
.\.venv\Scripts\activate

2) Lancer le pipeline complet
python src/train_pipeline.py

3) Résultat

Un fichier est généré automatiquement dans :

data/submission/

📒 Notebook d’analyse

Le fichier 01_data_analysis.ipynb contient :

Analyse exploratoire

Visualisations

Corrélations

Tests de plusieurs modèles

Validation croisée

Sélection du meilleur modèle

Il sert de zone d’expérimentation avant l'industrialisation du pipeline.

💡 Compétences développées

Construction d’un projet ML complet

Feature engineering avancé

Encodage et imputation intelligents

Cross-validation

Pipeline automatisé

Export et versioning des résultats

Industrialisation de code

👤 Auteur

Hamza Koubba
Data Scientist & IoT Engineer — Industrie 4.0 • IA & R&D

📧 hamzakoubba95@gmail.com

🔗 LinkedIn : https://www.linkedin.com/in/koubba/