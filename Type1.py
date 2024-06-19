import pandas as pd;

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv', index_col=0);
display(df);


# 인기동영상 제작횟수가 많은 채널 상위 10개명을 출력하라 (날짜기준, 중복포함)
# display(list(df.loc[df.channelId.isin(df.channelId.value_counts().head(10).index)].channelTitle.unique()));

# 논란으로 인기동영상이 된 케이스를 확인하고 싶다. dislikes수가 like 수보다 높은 동영상을 제작한 채널을 모두 출력하라
# display(list(df.loc[df.dislikes > df.likes].channelTitle.unique()));

# 채널명을 바꾼 케이스가 있는지 확인하고 싶다. channelId의 경우 고유값이므로 이를 통해 채널명을 한번이라도 바꾼 채널의 갯수를 구하여라
change = df[['channelId','channelTitle']].drop_duplicates().channelId.value_counts()
# display(len(change[change>1]));

# 일요일에 인기있었던 영상들중 가장많은 영상 종류(categoryId)는 무엇인가?
# display(df.loc[pd.to_datetime(df.trending_date2).dt.day_name() == 'Sunday'].categoryId.value_counts().index[0]);

# 각 요일별 인기 영상들의 categoryId는 각각 몇개 씩인지 하나의 데이터 프레임으로 표현하라
display((df.groupby([pd.to_datetime(df.trending_date2).dt.day_name(), 'categoryId'], as_index=False).size()).pivot(index='categoryId', columns='trending_date2'));