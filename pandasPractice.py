# 2024-06-09

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv", sep="\t")
#print(df);


#display(df.head(5));
a=df.shape
#print(a)

columns=df.columns
# print(columns);

# print(columns[5]);

# df[columns[5]].dtype

# df.index

# df[columns[5]][2];

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv', encoding='euc-kr')

# print(df.tail(3));

# print(df.info())

print(df.select_dtypes(exclude='object').columns);
print(df.select_dtypes(include='object').columns);

df.isnull().sum(axis=0);
