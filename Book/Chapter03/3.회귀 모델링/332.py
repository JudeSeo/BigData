# 분석 모형 구축

import pandas as pd;

data = pd.read_csv("../1.데이터 수집/housing_data.csv", header=None, sep=",");
col_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV',
             'isHighValue'];
data.columns = col_names
df_r = data.drop(['isHighValue'], axis=1);

# 01 데이터 분할
from sklearn.model_selection import train_test_split;

X_cols = ['LSTAT', 'PTRATIO', 'TAX', 'AGE', 'NOX', 'INDUS', 'CRIM']

X = df_r[X_cols].values;
y = df_r['MEDV'].values;

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y, test_size=0.3, random_state=123);

# 02 데이터 스케일링
from sklearn.preprocessing import MinMaxScaler;

scaler = MinMaxScaler();

X_train_r_scaled = scaler.fit_transform(X_train_r);
X_test_r_scaled = scaler.transform(X_test_r);

# 03 모델 구축
from sklearn.linear_model import LinearRegression;

model_lr = LinearRegression();
model_lr.fit(X_train_r_scaled, y_train_r);

# 04
print(model_lr.coef_);

# 05
print(model_lr.intercept_);

# 06 SVM
from sklearn.svm import SVR;

model_svr = SVR();
model_svr.fit(X_train_r_scaled, y_train_r);

# 07 랜덤포레스트
from sklearn.ensemble import RandomForestRegressor;

model_rfr = RandomForestRegressor(random_state=123);
model_rfr.fit(X_train_r_scaled, y_train_r);

# 08
for x, val in zip(X_cols, model_rfr.feature_importances_):
    print(f'{x} : %.3f' % val);
