# 데이터 전처리

import pandas as pd;
import numpy as np;

X_test = pd.read_csv("./yemoonsaBigdata/datasets/Part2/mpg_X_test.csv");
X_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/mpg_X_train.csv");
y_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/mpg_y_train.csv");

# 01
print(X_train.info());

# 02
from sklearn.impute import SimpleImputer;

imputer = SimpleImputer(missing_values=np.nan, strategy='mean');
X_train[['horsepower']] = imputer.fit_transform(X_train[['horsepower']]);
X_test[['horsepower']] = imputer.fit_transform(X_test[['horsepower']]);

# 03
print(X_train.describe());

# 04
COL_DEL = ['name'];
COL_NUM = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year'];
COL_CAT=[];
COL_Y=['isUSA'];

X_train = X_train.iloc[:,1:]
X_test = X_test.iloc[:,1:]