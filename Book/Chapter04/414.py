# 데이터 모형 구축
import pandas as pd;
import numpy as np;

X_test = pd.read_csv("./yemoonsaBigdata/datasets/Part2/mpg_X_test.csv");
X_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/mpg_X_train.csv");
y_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/mpg_y_train.csv");

COL_DEL = ['name'];
COL_NUM = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year'];
COL_CAT=[];
COL_Y=['isUSA'];

# 01
from sklearn.model_selection import train_test_split;
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.3);

# 02
from sklearn.preprocessing import StandardScaler;

scaler = StandardScaler();
scaler.fit(X_tr[COL_NUM]);
X_tr[COL_NUM] = scaler.transform(X_tr[COL_NUM]);
X_val[COL_NUM] = scaler.transform(X_val[COL_NUM]);
X_test[COL_NUM] = scaler.transform(X_test[COL_NUM]);

# 03
from sklearn.neighbors import KNeighborsClassifier;
modelKNN = KNeighborsClassifier(n_neighbors=5, metric='euclidean');
modelKNN.fit(X_tr, y_tr.values.ravel());

from sklearn.tree import DecisionTreeClassifier;
modelDT = DecisionTreeClassifier(max_depth=10);
modelDT.fit(X_tr, y_tr);