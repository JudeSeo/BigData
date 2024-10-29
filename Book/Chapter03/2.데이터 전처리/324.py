# 변수 변환

import pandas as pd;

data = pd.read_csv("../1.데이터 수집/housing_data.csv", header=None, sep=",");
col_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV',
             'isHighValue'];
data.columns = col_names

# 01
import matplotlib.pyplot as plt;
import seaborn as sns;

cols = data.columns;
fig, axs = plt.subplots(ncols=5, nrows=3, figsize=(20, 10));
idx = 0;
for _row in range(3):
    for _col in range(5):
        if idx < len(cols):
            sns.histplot(data[cols[idx]], ax=axs[_row][_col]);  # distplot가 deprecated 되어 histplot로 대체해서 사용
            idx += 1;

plt.tight_layout();

# 02
print(data.apply(lambda x: x.skew(), axis=0));

# 03
import numpy as np;

data["CRIM"] = np.log1p(data["CRIM"]);
print(data["CRIM"].skew());
