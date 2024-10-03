# 이상치 처리

import pandas as pd;

data = pd.read_csv("../1.데이터 수집/housing_data.csv", header=None, sep=",");
col_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV',
             'isHighValue'];
data.columns = col_names

# 01
import seaborn as sns;

sns.boxplot(data['MEDV']);

# 02
Q1, Q3 = data['MEDV'].quantile([0.25, 0.75]);
IQR = Q3 - Q1;
upper_bound = Q3 + 1.5 * IQR;
lower_bound = Q1 - 1.5 * IQR;

print("outlier 범위: %.2f 초과 또는 %.2f 미만" % (upper_bound, lower_bound));
print("outlier 개수: %.0f" % len(data[(data["MEDV"] > upper_bound) | (data["MEDV"] < lower_bound)]));
print("outlier 비율: %.2f" % (len(data[(data["MEDV"] > upper_bound) | (data["MEDV"] < lower_bound)]) / len(data)));


# 03
def get_outlier_prop(x):
    Q1, Q3 = x.quantile([0.25, 0.75]);
    IQR = Q3 - Q1;
    upper_bound = Q3 + 1.5 * IQR;
    lower_bound = Q1 - 1.5 * IQR;
    outliers = x[(x > upper_bound) | (x < lower_bound)];
    return str(round(100 * len(outliers) / len(x), 1)) + "%";


print(data.apply(get_outlier_prop));

# 04
Q1, Q3 = data["MEDV"].quantile([0.25, 0.75]);
IQR = Q3 - Q1;
upper_bound = Q3 + 1.5 * IQR;
lower_bound = Q1 - 1.5 * IQR;

data1 = data[(data["MEDV"] <= upper_bound) & (data["MEDV"] >= lower_bound)];
print(data1.shape);

# 05
data2 = data[~(data["MEDV"] >= 45)];
print(data2.shape);
