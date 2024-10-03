# 데이터 탐색

import pandas as pd;

data = pd.read_csv("../1.데이터 수집/housing_data.csv", header=None, sep=",");
col_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV',
             'isHighValue'];
data.columns = col_names

# 01
df_c = data.drop(['MEDV'], axis=1);
print(df_c);

# 02
import seaborn as sns;

sns.boxplot(x='isHighValue', y='LSTAT', data=df_c);

# 03
import seaborn as sns;

sns.kdeplot(df_c.loc[df_c['isHighValue'] == 1, 'LSTAT'], color='orange', fill=True);
sns.kdeplot(df_c.loc[df_c['isHighValue'] == 0, 'LSTAT'], color='blue', fill=True);

# 04
import numpy as np;

print(df_c.groupby('isHighValue').apply(np.mean).T);
