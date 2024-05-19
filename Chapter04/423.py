# 데이터 전처리

import pandas as pd;
import numpy as np;
import warnings;

warnings.filterwarnings('ignore');

X_test = pd.read_csv("./yemoonsaBigdata/datasets/Part2/penguin_X_test.csv");
X_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/penguin_X_train.csv");
y_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/penguin_y_train.csv");

# 01
print(X_train.info());

# 02
train=pd.concat([X_train, y_train], axis=1);
print(train.loc[(train.sex.isna())|(train.bill_length_mm.isna())|(train.bill_depth_mm.isna())|(train.flipper_length_mm.isna())|(train.body_mass_g.isna())]);

# 03
train = train.dropna();
train.reset_index(drop=True, inplace=True);

# 04
X_train = train[['species','island','sex','bill_length_mm','bill_depth_mm','flipper_length_mm']];
y_train = train[['body_mass_g']];

# 05
print(X_train.describe());

# 06
COL_DEL=[];
COL_NUM=['bill_length_mm','bill_depth_mm','flipper_length_mm'];
COL_CAT = ['species','island','sex'];
COL_Y=['body_mass_g'];

# 07
X = pd.concat([X_train, X_test]);

from sklearn.preprocessing import OneHotEncoder;
ohe = OneHotEncoder(handle_unknown='ignore');
ohe.fit(X[COL_CAT]);

X_train_res = ohe.transform(X_train[COL_CAT]);
X_test_res = ohe.transform(X_test[COL_CAT]);

# 08
print(X_train_res);

# 09
X_train_ohe = pd.DataFrame(X_train_res.todense(), columns=ohe.get_feature_names_out());
X_test_ohe = pd.DataFrame(X_test_res.todense(), columns=ohe.get_feature_names_out());
print(X_train_ohe);

X_train_fin = pd.concat([X_train[COL_NUM], X_train_ohe], axis=1);
X_test_fin = pd.concat([X_test[COL_NUM], X_test_ohe], axis=1);