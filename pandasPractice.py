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

# print(df.select_dtypes(exclude='object').columns);
# print(df.select_dtypes(include='object').columns);

# df.isnull().sum(axis=0);

# df.info();

# display(df.describe());

# print(df['거주인구']);

# quantile 사분위 수
# print(df['평균 속도'].quantile(0.75)-df['평균 속도'].quantile(0.25));

# nunique 유일값 수
# df['읍면동명'].nunique()

# unique 유일값
# df['읍면동명'].unique()

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv');
# type(df);

# loc
# df.loc[df['quantity']==3].head(5);

# reset_index(drop=True) 인덱스 처음부터 생성
# print(df.loc[df['quantity']==3].head(5).reset_index(drop=True))

# print(df[['quantity', 'item_price']]);

df['new_price'] = df['item_price'].str[1:].astype('float');
# print(df['new_price'].head());
# df.info();

# print(df.loc[df['new_price']<=5]);
# print(len(df.loc[df['new_price']<=5]));
