import pandas as pd
import numpy as np


def load_data(train_path, test_path):
    """Charge les fichiers train et test."""
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    return train, test


def combine_data(train, test):
    """Concatène train et test dans un seul DataFrame full."""
    train["Survived"] = train["Survived"].astype(float)
    test["Survived"] = np.nan  # placeholder pour aligner les colonnes
    full = pd.concat([train, test], ignore_index=True)
    return full


def feature_engineering(full):
    """Crée les features Title, FamilySize, Deck, FarePerPerson."""
    # Title (avec raw string pour éviter le warning \.)
    full["Title"] = full["Name"].str.extract(r' ([A-Za-z]+)\.', expand=False)
    full["Title"] = full["Title"].replace(['Mlle', 'Ms'], 'Miss')
    full["Title"] = full["Title"].replace(['Mme'], 'Mrs')
    full["Title"] = full["Title"].replace(
        ['Lady', 'Countess', 'Dona', 'Sir', 'Don', 'Jonkheer'], 'Noble'
    )
    full["Title"] = full["Title"].replace(
        ['Capt', 'Col', 'Major', 'Rev', 'Dr'], 'Officer'
    )

    # FamilySize
    full["FamilySize"] = full["SibSp"] + full["Parch"] + 1

    # Deck à partir de Cabin
    full["Deck"] = full["Cabin"].astype(str).str[0]
    full["Deck"] = full["Deck"].replace("n", "U")  # 'n' vient de 'nan'

    # Fare per person
    full["FarePerPerson"] = full["Fare"] / full["FamilySize"]

    return full


def fill_missing(full):
    """Imputation des valeurs manquantes (Embarked, Fare, Age)."""
    # Embarked : mode
    full["Embarked"] = full["Embarked"].fillna(full["Embarked"].mode()[0])

    # Fare : médiane
    full["Fare"] = full["Fare"].fillna(full["Fare"].median())

    # Age : médiane par Title
    full["Age"] = full.groupby("Title")["Age"].transform(
        lambda x: x.fillna(x.median())
    )

    return full


def remove_unused_columns(full):
    """
    Supprime les colonnes non utilisées comme features (mais laisse PassengerId).
    On garde PassengerId pour le fichier de soumission.
    """
    cols_to_drop = ["Name", "Ticket", "Cabin"]
    full = full.drop(cols_to_drop, axis=1, errors="ignore")
    return full


def encode_features(full):
    """One-Hot Encoding sur les colonnes catégorielles."""
    categorical_cols = ["Sex", "Embarked", "Title", "Deck"]
    full_encoded = pd.get_dummies(full, columns=categorical_cols, drop_first=True)
    return full_encoded
