# 데이터프레임 데이터 조회
import pandas as pd;

# 01
housing_df = pd.read_csv("california_housing_train.csv");
print("단일 컬럼 데이터 조회: \n", housing_df['housing_median_age'].head(3));
print("\n 복수 컬럼 데이터 조회: \n", housing_df[['housing_median_age', 'total_rooms']].head(3));

# 02
print(housing_df[0:3])

# 03
print(housing_df[housing_df['housing_median_age'] == 30].head(3));

# 04
print(housing_df[
          (housing_df['housing_median_age'] > 30) &
          (housing_df['total_rooms'] < 100) &
          (housing_df['median_income'] > 10)
          ].head(3));

# 05
con1 = housing_df['housing_median_age'] > 30;
con2 = housing_df['total_rooms'] < 100;
con3 = housing_df['median_income'] > 10;

print(housing_df[con1 & con2 & con3].head(3));

# 06
print(housing_df.iloc[0, 2])

# 07
print(housing_df.loc[0, 'housing_median_age']);

# 08
print(housing_df.loc[0:4, 'housing_median_age']);

# 09
print(housing_df.loc[housing_df['housing_median_age'] == 30, ['housing_median_age', 'total_bedrooms']].head(3));
