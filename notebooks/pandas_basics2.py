import pandas as pd

#how many rows and columns
df = pd.read_csv('titanic.csv')
print(df.shape)

#for missing values
print(df.isnull().sum())

#one group by result
print(df.groupby('Pclass')['Age'].mean())

#cleaning

#fixing the column names
df.columns = df.columns.str.lower().str.replace(r'[^a-z0-9]+', '_')
print(df.columns)