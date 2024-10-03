# 데이터프레임 데이터 정렬과 집계
import pandas as pd;

# 01
housing_df = pd.read_csv("california_housing_train.csv");
housing_sorted = housing_df.sort_values(by=['housing_median_age']);
print(housing_sorted.head(3));

# 02
housing_sorted = housing_df.sort_values(by=['housing_median_age', 'total_rooms'], ascending=False);
print(housing_sorted.head(3));

# 03
print(housing_df.sum() / housing_df.count());

# 04
print(housing_df[['housing_median_age', 'total_rooms']].mean());

# 05
housing_groupby = housing_df.groupby('housing_median_age').mean();
print(housing_groupby.head(3));

# 06
housing_groupby = housing_df.groupby('housing_median_age')[['total_rooms', 'total_bedrooms']].mean();
print(housing_groupby.head(3));

# 07
housing_groupby = housing_df.groupby('housing_median_age')['total_rooms'].agg([min, max, sum]);
print(housing_groupby.head(3));
