# 데이터 탐색

import pandas as pd;

data = pd.read_csv("../1.데이터 수집/housing_data.csv", header=None, sep=",");
col_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV',
             'isHighValue'];
data.columns = col_names

# 01
df_r = data.drop(['isHighValue'], axis=1);
print(df_r);

# 02
cols = ['MEDV', 'LSTAT', 'RM', 'CHAS', 'RAD', 'TAX'];
print(df_r[cols].corr());
