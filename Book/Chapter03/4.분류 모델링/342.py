# 분석 모형 구축

import pandas as pd;

data = pd.read_csv("../1.데이터 수집/housing_data.csv", header=None, sep=",");
col_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV',
             'isHighValue'];
data.columns = col_names

# 01
from sklearn.model_selection import train_test_split;

X_cols = ['LSTAT', 'PTRATIO', 'TAX', 'AGE', 'NOX', 'INDUS', 'CRIM'];
X = data[X_cols].values;
y = data['isHighValue'].values;

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y, test_size=0.3, random_state=123);

# 02
from sklearn.preprocessing import MinMaxScaler;

scaler = MinMaxScaler();

X_train_c_scaled = scaler.fit_transform(X_train_c);
X_test_c_scaled = scaler.transform(X_test_c);

# 03
from sklearn.linear_model import LinearRegression;

model_lo = LinearRegression();
model_lo.fit(X_train_c_scaled, y_train_c);

# 04
print(model_lo.coef_);

# 05
print(model_lo.intercept_);

# 06 SVM
from sklearn.svm import SVC;

model_svc = SVC(probability=True);
model_svc.fit(X_train_c_scaled, y_train_c);

# 07 랜덤포레스트
from sklearn.ensemble import RandomForestClassifier;

model_rfc = RandomForestClassifier(random_state=123);
model_rfc.fit(X_train_c_scaled, y_train_c);

# 08
for x, val in zip(X_cols, model_rfc.feature_importances_):
    print(f'{x} : %.3f' % val);
