# 🧮 Titanic Statistical Analysis

### 🎯 Objectif du projet
Ce projet a pour objectif de réaliser une **analyse statistique descriptive** ainsi qu’un pipeline Machine Learning complet sur le célèbre dataset Titanic afin de comprendre les facteurs influençant la survie et de construire un modèle prédictif fiable.

Il fait partie d’une série de mini-projets personnels pour renforcer mes bases en **mathématiques appliquées à la data science**.

---

### 📊 Données utilisées
Le dataset provient du concours open source **[Titanic - Machine Learning from Disaster (Kaggle)](https://www.kaggle.com/c/titanic/data)**.

Il contient les principales informations sur les passagers :
- `Survived` : 1 = a survécu, 0 = n’a pas survécu  
- `Pclass` : classe du billet (1ère, 2e, 3e)  
- `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, `Embarked`, etc.

---

### 🔧 Outils et librairies utilisés
- **Python 3.13**
- **Jupyter Notebook**
- **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn**
- **SciPy**

---

### 🚀 Étapes principales

1. Analyse Statistique (EDA)

- Exploration du dataset
- Analyse des distributions : âge, tarifs, classes
- Étude des corrélations avec la survie
- Visualisations explicatives (heatmaps, barplots, KDE…)

2. Nettoyage des données

- Gestion des valeurs manquantes
- Age imputé par médiane selon le Title
- Embarked imputé par le mode
- Fare imputé par médiane
- Normalisation et structuration des colonnes
- Suppression de Name, Ticket, Cabin

3. Feature Engineering avancé

-Ajout de nouvelles variables pertinentes :
-Title (extrait de Name)
-Deck (extrait de Cabin)
-FamilySize = SibSp + Parch + 1
-FarePerPerson = Fare / FamilySize
-Age*Class (pas necessaire)

4. Encodage

-One-Hot Encoding global sur : Sex, Embarked, Title, Deck
-Alignement parfait entre train & test

5. Entraînement du modèle

-Modèle utilisé : RandomForestClassifier
-Hyperparamètres choisis :

- n_estimators = 300

- max_depth = 6

- min_samples_split = 5

- min_samples_leaf = 2

- random_state = 42

- n_jobs = -1

6. Validation

-Cross-validation 5-fold
-Résultat moyen : ~0.827

7. Génération automatique des fichiers Kaggle

-Prédiction sur le dataset test
-Export automatique : data/submission/submission_random_forest_YYYYMMDD_HHMMSS.csv

---

### 💡 Compétences renforcées
- Statistiques descriptives appliquées
- Preprocessing propre & structuré
- Feature engineering pertinent
- Gestion avancée des valeurs manquantes
- Création d’un pipeline ML reproductible
- Cross-validation & tuning de modèle
- Génération automatisée de résultats

---

### 📁 Organisation du projet

01_titanic_statistical_analysis/
├── data/                 # Données train/test + submission
├── notebooks/
│   └── 01_data_analysis.ipynb
├── src/
│   ├── preprocessing.py
│   ├── model_random_forest.py
│   └── train_pipeline.py
├── images/              # Graphiques exportés (optionnel)
├── README.md
├── requirements.txt
└── .gitignore



---

### 👤 Auteur
**Hamza Koubba**  
*Data Scientist | Industry 4.0 | R&D*  
📧 hamzakoubba95@gmail.com  
🔗 [linkedin.com/in/koubba](https://www.linkedin.com/in/koubba/)