# 1) Charger les données
# 2) Concatener train/test
# 3) Feature engineering (Title, FamilySize, Deck, FarePerPerson)
# 4) Imputer les valeurs manquantes
# 5) Supprimer les colonnes inutiles
# 6) One-Hot Encoding
# 7) Re-séparer train/test
# 8) Entraîner le modèle
# 9) Prédire et générer la submission

import pandas as pd
from src.preprocessing import (
    load_data,
    combine_data,
    feature_engineering,
    fill_missing,
    remove_unused_columns,
    encode_features,
)
from src.model_random_forest import train_random_forest


def run_training():
    # 1) Charger les données brutes
    train, test = load_data("data/train.csv", "data/test.csv")

    # 2) Concaténer
    full = combine_data(train, test)

    # 3) Feature engineering
    full = feature_engineering(full)

    # 4) Imputation des NaN
    full = fill_missing(full)

    # 5) Supprimer les colonnes non utiles (Name, Ticket, Cabin)
    full = remove_unused_columns(full)

    # 6) One-Hot Encoding global sur full (train + test)
    full_encoded = encode_features(full)

    # 7) Re-séparer train/test
    len_train = len(train)
    train_encoded = full_encoded.iloc[:len_train].copy()
    test_encoded = full_encoded.iloc[len_train:].copy()

    # 8) X_train, y_train, X_test (on enlève PassengerId des features)
    X_train = train_encoded.drop(["Survived", "PassengerId"], axis=1, errors="ignore")
    y_train = train_encoded["Survived"]
    X_test = test_encoded.drop(["Survived", "PassengerId"], axis=1, errors="ignore")

    # 9) Entraîner le modèle
    model = train_random_forest(X_train, y_train)

    # 10) Prédire
    y_pred = model.predict(X_test)

    # 11) Construire la submission (PassengerId vient du test original)
    submission = pd.DataFrame({
        "PassengerId": test["PassengerId"],
        "Survived": y_pred
    })

        # 12) Sauvegarde avec un nom unique basé sur la date/heure
    from datetime import datetime
    import os
    
    # Créer le dossier s'il n'existe pas
    os.makedirs("data/submission", exist_ok=True)

    # Timestamp : AAAAMMJJ_HHMMSS
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/submission/submission_random_forest_{timestamp}.csv"

    submission.to_csv(filename, index=False)
    print(f"Submission saved at {filename}")



if __name__ == "__main__":
    run_training()
