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


# print(df.loc[df['item_name']=='Chicken Salad Bowl'].reset_index(drop=True));

# print(df.loc[(df['new_price']<=9) & (df['item_name']=='Chicken Salad Bowl')]);

# print(df.sort_values('new_price', ascending=True).reset_index(drop=True));

# print(df.loc[df['item_name'].str.contains('Chips')]);

# 짝수번째 컬럼만 출력
# print(df);
# display(df.iloc[:,::2]);

# df의 new_price 컬럼 값에 따라 내림차순으로 정리하고 index를 초기화 하여라
# display(df.sort_values('new_price', ascending=False).reset_index(drop=True));


# df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 인덱싱하라
# display(df.loc[(df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')]);

# df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 첫번째 케이스만 남겨라
# display(df.loc[(df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')].drop_duplicates('item_name'));

# df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 마지막 케이스만 남겨라
# display(df.loc[(df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')].drop_duplicates('item_name', keep='last'));

# df의 데이터 중 new_price값이 new_price값의 평균값 이상을 가지는 데이터들을 인덱싱하라
# display(df.loc[df['new_price'] >= df['new_price'].mean()]);

# df의 데이터 중 item_name의 값이 Izze 데이터를 Fizzy Lizzy로 수정하라
# df.loc[df['item_name'] == 'Izze', 'item_name'] = 'Fizzy Lizzy';
# display(df);

# df의 데이터 중 choice_description 값이 NaN 인 데이터의 갯수를 구하여라
# display(df.choice_description.isnull().sum());

# df의 데이터 중 choice_description 값이 NaN 인 데이터를 NoData 값으로 대체하라(loc 이용)
df.loc[df.choice_description.isnull(), 'choice_description'] = 'NoData'
# display(df)

# df의 데이터 중 choice_description 값에 Black이 들어가는 경우를 인덱싱하라
# display(df.loc[df.choice_description.str.contains('Black')])
# 값에 null이 있으면 에러남

# df의 데이터 중 choice_description 값에 Vegetables 들어가지 않는 경우의 갯수를 출력하라
# display(len(df.loc[~df.choice_description.str.contains('Vegetables')]))

# df의 데이터 중 item_name 값이 N으로 시작하는 데이터를 모두 추출하라
# display(df[df.item_name.str.startswith('N')]);

# df의 데이터 중 item_name 값의 단어갯수가 15개 이상인 데이터를 인덱싱하라
# display(df[df.item_name.str.len() >= 15]);

# df의 데이터 중 new_price값이 lst에 해당하는 경우의 데이터 프레임을 구하고 그 갯수를 출력하라 lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
# list = [1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98];
# ans = df[df.new_price.isin(list)];
# display(ans)
# display(len(ans));
