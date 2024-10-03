# 결측치 처리

import pandas as pd;

data = pd.read_csv("../1.데이터 수집/housing_data.csv", header=None, sep=",");
col_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV',
             'isHighValue'];
data.columns = col_names

# 01
print(data.isnull().sum());

# 02
print(data.isnull().sum()/data.shape[0]);

# 03
data1 = data.copy();
med_val = data['CRIM'].median();
data1['CRIM'] = data1['CRIM'].fillna(med_val);

# 04
data = data.loc[data['CRIM'].notnull(), ];
print(data.describe());