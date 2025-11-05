import pandas as pd

train=pd.read_csv('data/train.csv')
test=pd.read_csv('data/test.csv')   
gender_submission=pd.read_csv('data/gender_submission.csv')

print("=== train SET ===")
print(train.shape)
print(train.columns)
print("\n=== test SET ===")
print(test.shape)
print(test.columns)
print("\n=== gender_submission SET ===")
print(gender_submission.head())