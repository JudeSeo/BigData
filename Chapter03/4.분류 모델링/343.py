# 분석 모형 평가

import pandas as pd;

data = pd.read_csv("../1.데이터 수집/housing_data.csv", header=None, sep=",");
col_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV',
             'isHighValue'];
data.columns = col_names

from sklearn.model_selection import train_test_split;

X_cols = ['LSTAT', 'PTRATIO', 'TAX', 'AGE', 'NOX', 'INDUS', 'CRIM'];
X = data[X_cols].values;
y = data['isHighValue'].values;
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y, test_size=0.3, random_state=123);

from sklearn.preprocessing import MinMaxScaler;

scaler = MinMaxScaler();
X_train_c_scaled = scaler.fit_transform(X_train_c);
X_test_c_scaled = scaler.transform(X_test_c);

from sklearn.linear_model import LinearRegression;

model_lo = LinearRegression();
model_lo.fit(X_train_c_scaled, y_train_c);

from sklearn.svm import SVC;

model_svc = SVC(probability=True);
model_svc.fit(X_train_c_scaled, y_train_c);

from sklearn.ensemble import RandomForestClassifier;

model_rfc = RandomForestClassifier(random_state=123);
model_rfc.fit(X_train_c_scaled, y_train_c);

# 01
y_pred_lo = model_lo.predict(X_test_c_scaled);
y_pred_svc = model_svc.predict(X_test_c_scaled);
y_pred_rfc = model_rfc.predict(X_test_c_scaled);

# 02
from sklearn.metrics import classification_report;

print('-' * 60);
print('로지스틱 회귀 결과');
print(classification_report(y_test_c, y_pred_lo, labels=[0, 1]));
print('-' * 60);
print('SVM 결과');
print(classification_report(y_test_c, y_pred_svc, labels=[0, 1]));
print('-' * 60);
print('랜덤포레스트 결과');
print(classification_report(y_test_c, y_pred_rfc, labels=[0, 1]));
print('-' * 60);

# 03
from sklearn.metrics import roc_auc_score;

y_pred_lo = model_lo.predict_proba(X_test_c_scaled)[:, 1];
y_pred_svc = model_svc.predict_proba(X_test_c_scaled)[:, 1];
y_pred_rfc = model_rfc.predict_proba(X_test_c_scaled)[:, 1];

print('로지스틱 회귀 결과: %.3f' % roc_auc_score(y_test_c, y_pred_lo));
print('SVM 결과: %.3f' % roc_auc_score(y_test_c, y_pred_svc));
print('랜덤포레스트 결과: %.3f' % roc_auc_score(y_test_c, y_pred_rfc));
