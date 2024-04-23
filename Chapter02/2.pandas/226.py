# 데이터프레임 데이터 삭제
import pandas as pd;

# 01
housing_df = pd.read_csv("california_housing_train.csv");
housing_df['Age_0'] = 0;
housing_df['Age_by_10'] = housing_df['housing_median_age'] // 10;
housing_df['Age_by_10'] = housing_df['Age_by_10'] * 10;
housing_drop_df = housing_df.drop('Age_0', axis=1);
print(housing_drop_df.head(3));

# 02
drop_result = housing_df.drop(['Age_0', 'Age_by_10'], axis=1, inplace=True);
print('drop_result 반환값: ', drop_result);
print(housing_df.head(3));

# 03
housing_drop_df = housing_df.drop([0, 1, 2], axis=0);
print(housing_drop_df.head(3));
