# 데이터 모형 구축

import pandas as pd;
import numpy as np;
import warnings;

warnings.filterwarnings('ignore');

X_test = pd.read_csv("./yemoonsaBigdata/datasets/Part2/penguin_X_test.csv");
X_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/penguin_X_train.csv");
y_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/penguin_y_train.csv");
train=pd.concat([X_train, y_train], axis=1);

from sklearn.preprocessing import OneHotEncoder;
ohe = OneHotEncoder(handle_unknown='ignore');
ohe.fit(X[COL_CAT]);
X_train = train[['species','island','sex','bill_length_mm','bill_depth_mm','flipper_length_mm']];
y_train = train[['body_mass_g']];
COL_DEL=[];
COL_NUM=['bill_length_mm','bill_depth_mm','flipper_length_mm'];
COL_CAT = ['species','island','sex'];
COL_Y=['body_mass_g'];
X_train_res = ohe.transform(X_train[COL_CAT]);
X_test_res = ohe.transform(X_test[COL_CAT]);
X_train_ohe = pd.DataFrame(X_train_res.todense(), columns=ohe.get_feature_names_out());
X_test_ohe = pd.DataFrame(X_test_res.todense(), columns=ohe.get_feature_names_out());

X_train_fin = pd.concat([X_train[COL_NUM], X_train_ohe], axis=1);
X_test_fin = pd.concat([X_test[COL_NUM], X_test_ohe], axis=1);
# 01
from sklearn.model_selection import train_test_split;
X_tr, X_val, y_tr, y_val = train_test_split(X_train_fin, y_train, test_size=0.3);

# 02
from sklearn.preprocessing import MinMaxScaler;

scaler=MinMaxScaler();
scaler.fit(X_tr[COL_NUM]);
X_tr[COL_NUM]=scaler.transform(X_tr[COL_NUM]);
X_val[COL_NUM]=scaler.transform(X_val[COL_NUM]);
X_test_fin[COL_NUM]=scaler.transform(X_test_fin[COL_NUM]);

# 03
from sklearn.linear_model import LinearRegression;

modelLR = LinearRegression();
modelLR.fit(X_tr, y_tr);

y_val_pred = modelLR.predict(X_val);
print(y_val_pred);

# 04
print(modelLR.intercept_);

coef = pd.Series(data=modelLR.coef_[0], index=X_train_fin.columns);
print(coef.sort_values());