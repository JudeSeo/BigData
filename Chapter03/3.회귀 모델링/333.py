# 분석 모형 평가

import pandas as pd;

data = pd.read_csv("../1.데이터 수집/housing_data.csv", header=None, sep=",");
col_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV',
             'isHighValue'];
data.columns = col_names
df_r = data.drop(['isHighValue'], axis=1);

from sklearn.model_selection import train_test_split;

X_cols = ['LSTAT', 'PTRATIO', 'TAX', 'AGE', 'NOX', 'INDUS', 'CRIM']

X = df_r[X_cols].values;
y = df_r['MEDV'].values;

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y, test_size=0.3, random_state=123);

from sklearn.preprocessing import MinMaxScaler;

scaler = MinMaxScaler();

X_train_r_scaled = scaler.fit_transform(X_train_r);
X_test_r_scaled = scaler.transform(X_test_r);

from sklearn.linear_model import LinearRegression;

model_lr = LinearRegression();
model_lr.fit(X_train_r_scaled, y_train_r);

from sklearn.svm import SVR;

model_svr = SVR();
model_svr.fit(X_train_r_scaled, y_train_r);

from sklearn.ensemble import RandomForestRegressor;

model_rfr = RandomForestRegressor(random_state=123);
model_rfr.fit(X_train_r_scaled, y_train_r);

# 01
y_pred_lr = model_lr.predict(X_test_r_scaled);
y_pred_svr = model_svr.predict(X_test_r_scaled);
y_pred_rfr = model_rfr.predict(X_test_r_scaled);

# 02
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error;

print('-' * 30);
print('선형 회귀 결과');
print('MAE: %.3f' % mean_absolute_error(y_test_r, y_pred_lr));
print('MSE: %.3f' % mean_squared_error(y_test_r, y_pred_lr));
print('MAPE: %.3f' % mean_absolute_percentage_error(y_test_r, y_pred_lr));
print('-' * 30);
print('SVM 결과');
print('MAE: %.3f' % mean_absolute_error(y_test_r, y_pred_svr));
print('MSE: %.3f' % mean_squared_error(y_test_r, y_pred_svr));
print('MAPE: %.3f' % mean_absolute_percentage_error(y_test_r, y_pred_svr));
print('-' * 30);
print('랜덤포레스트 결과');
print('MAE: %.3f' % mean_absolute_error(y_test_r, y_pred_rfr));
print('MSE: %.3f' % mean_squared_error(y_test_r, y_pred_rfr));
print('MAPE: %.3f' % mean_absolute_percentage_error(y_test_r, y_pred_rfr));
print('-' * 30);
