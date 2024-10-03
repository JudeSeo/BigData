# 데이터프레임 결측치 처리하기
import numpy as np;
import pandas as pd;

# 01
housing_df = pd.read_csv("california_housing_train.csv");
housing_df['Age_na'] = np.nan;
print(housing_df.isna().head(3));

# 02
print(housing_df.isna().sum());

# 03
housing_df['Age_na'] = housing_df['Age_na'].fillna(housing_df['housing_median_age'].mean());
print(housing_df.head(3));
