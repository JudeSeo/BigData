# 데이터프레임 컬럼 생성과 수정
import pandas as pd;

# 01
housing_df = pd.read_csv("california_housing_train.csv");
housing_df['Age_0'] = 0;
print(housing_df.head(3));

# 02
housing_df['Age_by_10'] = housing_df['housing_median_age'] // 10;
print(housing_df.head(3));

# 03
housing_df['Age_by_10'] = housing_df['Age_by_10'] * 10;
print(housing_df.head(3));

# 04
value_counts = housing_df['Age_by_10'].value_counts();
print(value_counts);
