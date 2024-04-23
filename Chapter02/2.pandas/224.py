# 데이터프레임 훑어보기
import pandas as pd;

# 01
housing_df = pd.read_csv("california_housing_train.csv");
print("DataFrame 크기: ", housing_df.shape);
print(housing_df.head(5));

# 02
print(housing_df.info());

# 03
print(housing_df.describe());

# 04
housing_median_age = housing_df['housing_median_age'];
print(housing_median_age.head());

# 05
value_counts = housing_median_age.value_counts();
print(value_counts);
