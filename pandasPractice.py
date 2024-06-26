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

# 데이터를 로드하고 상위 5개 컬럼을 출력하라
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv');
# display(df.head(5));

# 데이터의 각 host_name의 빈도수를 구하고 host_name으로 정렬하여 상위 5개를 출력하라
# display(df.describe());
# display(df.groupby('host_name').size().head(5));
# display(df.host_name.value_counts().sort_index().head(5));

# 데이터의 각 host_name의 빈도수를 구하고 빈도수 기준 내림차순 정렬한 데이터 프레임을 만들어라. 빈도수 컬럼은 counts로 명명하라
# display(df.groupby('host_name').size().to_frame().rename(columns={0:'counts'}).sort_values('counts', ascending=False));

# neighbourhood_group의 값에 따른 neighbourhood컬럼 값의 갯수를 구하여라
# display(df.groupby(['neighbourhood_group', 'neighbourhood'], as_index=False).size());

# neighbourhood_group의 값에 따른 neighbourhood컬럼 값 중 neighbourhood_group그룹의 최댓값들을 출력하라
# display(df.groupby(['neighbourhood_group', 'neighbourhood'], as_index=False).size().groupby('neighbourhood_group', as_index=False).max());

# neighbourhood_group 값에 따른 price값의 평균, 분산, 최대, 최소 값을 구하여라
# display(df.groupby('neighbourhood_group').agg({'price':['mean', 'var', 'max', 'min']}));
# display(df[['neighbourhood_group','price']].groupby('neighbourhood_group').agg({'price':['mean', 'var', 'max', 'min']}));

# neighbourhood_group 값에 따른 reviews_per_month 평균, 분산, 최대, 최소 값을 구하여라
# display(df.groupby('neighbourhood_group').agg({'reviews_per_month':['mean','var','max','min']}));
# display(df[['neighbourhood_group','reviews_per_month']].groupby('neighbourhood_group').agg(['mean','var','max','min']));

# neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 구하라
# display(df.groupby(['neighbourhood', 'neighbourhood_group']).price.mean());

# neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하라
# display(df.groupby(['neighbourhood', 'neighbourhood_group']).price.mean().unstack());

# neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하고 nan 값은 -999값으로 채워라
# display(df.groupby(['neighbourhood', 'neighbourhood_group']).price.mean().unstack().fillna(-999));

# 데이터중 neighbourhood_group 값이 Queens값을 가지는 데이터들 중 neighbourhood 그룹별로 price값의 평균, 분산, 최대, 최소값을 구하라
# display(df[df.neighbourhood_group == "Queens"].groupby(['neighbourhood']).agg({'price':['mean', 'var','max','min']}));

# *************************************************
# 데이터중 neighbourhood_group 값에 따른 room_type 컬럼의 숫자를 구하고 neighbourhood_group 값을 기준으로 각 값의 비율을 구하여라
# ans = df[['neighbourhood_group', 'room_type']].groupby(['neighbourhood_group', 'room_type']).size().unstack();
# ans.loc[:,:]=(ans.values/ans.sum(axis=1).values.reshape(-1,1))
# display(ans);

# ~55



# 데이터를 로드하고 데이터 행과 열의 갯수를 출력하라
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/BankChurnersUp.csv');
# display(df.shape);

# Income_Category의 카테고리를 map 함수를 이용하여 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
# Unknown : N
# Less than $40K : a
# $40K - $60K : b
# $60K - $80K : c
# $80K - $120K : d
# $120K +’ : e

# dic={
# 'Unknown' : 'N',
# 'Less than $40K' : 'a',
# '$40K - $60K' : 'b',
# '$60K - $80K' : 'c',
# '$80K - $120K' : 'd',
# '$120K +' : 'e',
# }
# df['newIncome'] = df.Income_Category.map(lambda x:dic[x]);
# display(df['newIncome'])


# Income_Category의 카테고리를 apply 함수를 이용하여 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
# Unknown : N
# Less than $40K : a
# $40K - $60K : b
# $60K - $80K : c
# $80K - $120K : d
# $120K +’ : e

# def changeCategory(x):
#     if x =='Unknown':
#         return 'N'
#     elif x =='Less than $40K':
#         return 'a'
#     elif x =='$40K - $60K':
#         return 'b'
#     elif x =='$60K - $80K':
#         return 'c'
#     elif x =='$80K - $120K':
#         return 'd'
#     elif x =='$120K +' :
#         return 'e'

# df['new_Income'] = df.Income_Category.apply(lambda x:changeCategory(x));
# display(df['new_Income']);


# Customer_Age의 값을 이용하여 나이 구간을 AgeState 컬럼으로 정의하라. (0~9 : 0 , 10~19 :10 , 20~29 :20 … 각 구간의 빈도수를 출력하라
# df['AgeState'] = df.Customer_Age.map(lambda x:x//10*10);
# display(df.groupby('AgeState').size());

# Education_Level의 값중 Graduate단어가 포함되는 값은 1 그렇지 않은 경우에는 0으로 변경하여 newEduLevel 컬럼을 정의하고 빈도수를 출력하라
# df['newEduLevel'] = df.Education_Level.map(lambda x: 1 if "Graduate" in x else 0);
# display(df.groupby('newEduLevel').size());
# display(df['newEduLevel'].value_counts());

# Credit_Limit 컬럼값이 4500 이상인 경우 1 그외의 경우에는 모두 0으로 하는 newLimit 정의하라. newLimit 각 값들의 빈도수를 출력하라
# df['newLimit'] = df.Credit_Limit.map(lambda x: 1 if x >= 4500 else 0);
# display(df['newLimit'].value_counts());

# Marital_Status 컬럼값이 Married 이고 Card_Category 컬럼의 값이 Platinum인 경우 1 그외의 경우에는 모두 0으로 하는 newState컬럼을 정의하라. newState의 각 값들의 빈도수를 출력하라
# def changeCategory(x):
#     if x.Marital_Status =='Married' and x.Card_Category == 'Platinum':
#         return 1
#     else:
#         return 0

# df['newState'] = df.apply(changeCategory, axis=1);
# display(df['newState'].value_counts());

# Gender 컬럼값 M인 경우 male F인 경우 female로 값을 변경하여 Gender 컬럼에 새롭게 정의하라. 각 value의 빈도를 출력하라
# def changeGender(x):
#     if x == 'M': return 'male';
#     else: return 'female';

# df['Gender'] = df.Gender.apply(changeGender);
# display(df['Gender'].value_counts());


df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv');
# display(df.info());

# Yr_Mo_Dy을 판다스에서 인식할 수 있는 datetime64타입으로 변경하라
df.Yr_Mo_Dy = pd.to_datetime(df.Yr_Mo_Dy)
# display(df);

# Yr_Mo_Dy에 존재하는 년도의 유일값을 모두 출력하라
# display(df.Yr_Mo_Dy.dt.year.unique());

# Yr_Mo_Dy에 년도가 2061년 이상의 경우에는 모두 잘못된 데이터이다. 해당경우의 값은 100을 빼서 새롭게 날짜를 Yr_Mo_Dy 컬럼에 정의하라
def checkYear(x):
    import datetime;
    if x.year >= 2061:
        return pd.to_datetime(datetime.date(x.year-100, x.month, x.day))
    else:
        return pd.to_datetime(datetime.date(x.year, x.month, x.day))
df['Yr_Mo_Dy'] = df.Yr_Mo_Dy.apply(checkYear)
# display(df);

# 년도별 각컬럼의 평균값을 구하여라
# display(df.groupby(df.Yr_Mo_Dy.dt.year).mean());

# weekday컬럼을 만들고 요일별로 매핑하라 ( 월요일: 0 ~ 일요일 :6)
df['weekday'] = df.Yr_Mo_Dy.dt.weekday;
# display(df['weekday'].to_frame());

# weekday컬럼을 기준으로 주말이면 1 평일이면 0의 값을 가지는 WeekCheck 컬럼을 만들어라
df['WeekCheck'] = df.weekday.map(lambda x: 1 if x in [5,6] else 0);
# display(df['WeekCheck'].to_frame());

# 년도, 일자 상관없이 모든 컬럼의 각 달의 평균을 구하여라
# display(df.groupby(df.Yr_Mo_Dy.dt.month).mean());

# 모든 결측치는 컬럼기준 직전의 값으로 대체하고 첫번째 행에 결측치가 있을경우 뒤에있는 값으로 대채하라
df=df.fillna(method='ffill').fillna(method='bfill');
# display(df);

# 년도 - 월을 기준으로 모든 컬럼의 평균값을 구하여라
# display(df.groupby(df.Yr_Mo_Dy.dt.to_period('M')).mean());

# RPT 컬럼의 값을 일자별 기준으로 1차차분하라
# display(df['RPT'].diff());

# RPT와 VAL의 컬럼을 일주일 간격으로 각각 이동평균한값을 구하여라
# display(df[['RPT', 'VAL']].rolling(7).mean());

# 서울시 미세먼지
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/seoul_pm.csv');

# 년-월-일:시 컬럼을 pandas에서 인식할 수 있는 datetime 형태로 변경하라. 서울시의 제공데이터의 경우 0시가 24시로 표현된다
def change_date(x):
    import datetime;
    hour = x.split(':')[1]
    date = x.split(":")[0]

    if hour =='24':
        hour ='00:00:00'

        FinalDate = pd.to_datetime(date +" "+hour) +datetime.timedelta(days=1)

    else:
        hour = hour +':00:00'
        FinalDate = pd.to_datetime(date +" "+hour)

    return FinalDate;

df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change_date)
# display(df);

# 일자별 영어요일 이름을 dayName 컬럼에 저장하라
df['dayName'] = df['(년-월-일:시)'].dt.day_name();
# display(df['dayName']);

# 일자별 각 PM10등급의 빈도수를 파악하라
ans=df.groupby(['dayName','PM10등급'], as_index=False).size();
# display(ans);
# display(ans.pivot(index='dayName',columns='PM10등급', values='size').fillna(0));

# 시간이 연속적으로 존재하며 결측치가 없는지 확인하라
check = len(df['(년-월-일:시)'].diff().unique());
# if check == 2:
#     print(True);
# else :
#     print(False);

# 오전 10시와 오후 10시(22시)의 PM10의 평균값을 각각 구하여라
# display(df.groupby(df['(년-월-일:시)'].dt.hour)['PM10'].mean().iloc[[10, 22]]);


# 날짜 컬럼을 index로 만들어라
df.set_index('(년-월-일:시)', inplace=True, drop=True)
# display(df);

# 데이터를 주단위로 뽑아서 최소,최대 평균, 표준표차를 구하여라
# display(df.index)
ans = df.select_dtypes(exclude='object').resample('W').agg(['min','max','mean','var']);
# display(ans);

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/under5MortalityRate.csv');
# Indicator을 삭제하고 First Tooltip 컬럼에서 신뢰구간에 해당하는 표현을 지워라
df.drop('Indicator', axis=1, inplace=True);
df['First Tooltip'] = df['First Tooltip'].map(lambda x:float(x.split("[")[0]));
# display(df);

# 년도가 2015년 이상, Dim1이 Both sexes인 케이스만 추출하라
ans = df.loc[(df['Period']>=2015) & (df['Dim1'] == 'Both sexes')]
# display(ans)

# 84번 문제에서 추출한 데이터로 아래와 같이 나라에 따른 년도별 사망률을 데이터 프레임화 하라
ans2 = ans.pivot(index='Location', columns='Period', values='First Tooltip')
# display(ans2);

# Dim1에 따른 년도별 사망비율의 평균을 구하라
ans = df.pivot_table(index='Dim1',columns='Period',values='First Tooltip', aggfunc='mean');
# display(ans);


df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/winter.csv');
# display(df);
# 데이터에서 한국 KOR 데이터만 추출하라
# display(df.loc[df['Country'] == 'KOR']);

# 한국 올림픽 메달리스트 데이터에서 년도에 따른 medal 갯수를 데이터프레임화 하라
# display(df.loc[df['Country'] == 'KOR'].pivot_table(index='Year',columns='Medal', aggfunc='size').fillna(0));

# 전체 데이터에서 sport종류에 따른 성별수를 구하여라
# display(df.pivot_table(index='Sport',columns='Gender', aggfunc='size'));

# 전체 데이터에서 Discipline종류에 따른 따른 Medal수를 구하여라
# display(df.pivot_table(index='Discipline',columns='Medal', aggfunc='size'));


df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv',index_col= 0);

df1 = df.iloc[:4,:]
df2 = df.iloc[4:,:]

# display(df1)
# display(df2)

# df1과 df2 데이터를 하나의 데이터 프레임으로 합쳐라
# display(pd.concat([df1,df2]));

df3 = df.iloc[:2,:4]
df4 = df.iloc[5:,3:]

# display(df3);
# display(df4);

# df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 둘다 포함하고 있는 년도에 대해서만 고려한다
# help(pd.concat)
# display(pd.concat([df3, df4], join='inner'));

# df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 모든 컬럼을 포함하고, 결측치는 0으로 대체한다
# display(pd.concat([df3, df4], join='outer').fillna(0));

df5 = df.T.iloc[:7,:3]
df6 = df.T.iloc[6:,2:5]

# display(df5)
# display(df6)

# df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 두 데이터 모두 포함하는 데이터만 출력하라
# help(pd.merge);
# display(pd.merge(df5,df6, how='inner', on='Algeria'));

# df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 합집합으로 합쳐라
# display(pd.merge(df5, df6, on='Algeria', how='outer'));