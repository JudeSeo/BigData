# 데이터 모델 평가
import pandas as pd;
import numpy as np;

X_test = pd.read_csv("./yemoonsaBigdata/datasets/Part2/mpg_X_test.csv");
X_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/mpg_X_train.csv");
y_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/mpg_y_train.csv");

from sklearn.model_selection import train_test_split;
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.3);

from sklearn.neighbors import KNeighborsClassifier;
modelKNN = KNeighborsClassifier(n_neighbors=5, metric='euclidean');
modelKNN.fit(X_tr, y_tr.values.ravel());

from sklearn.tree import DecisionTreeClassifier;
modelDT = DecisionTreeClassifier(max_depth=10);
modelDT.fit(X_tr, y_tr);

# 01
y_val_pred = modelKNN.predict(X_val);

y_val_pred_probaKNN = modelKNN.predict_proba(X_val);
y_val_pred_probaDT = modelDT.predict_proba(X_val);

# 02
from sklearn.metrics import roc_auc_score;

scoreKNN = roc_auc_score(y_val, y_val_pred_probaKNN[:,1]);
scoreDT = roc_auc_score(y_val, y_val_pred_probaDT[:,1]);

print(scoreKNN, scoreDT);

# 03
best_model = None;
best_score = 0;

for i in range(2, 10):
    model = KNeighborsClassifier(n_neighbors=i, metric='euclidean');
    model.fit(X_tr, y_tr.values.ravel());
    y_val_pred_proba = model.predict_proba(X_val);
    score = roc_auc_score(y_val, y_val_pred_proba[:,1]);
    print(i, "개의 이웃 확인 : ", score);

    # 뭔가 이상하게 여기서 에러남... 자료형 안 맞는다고 하는데... 틀린건 없어보임..
    # best_score가 아니라 best_model였음..
    if best_score <= score:
        best_model = model

# 04
print(best_model.predict_proba(X_test));

# 05
pred = best_model.predict_proba(X_test)[:,1]
print(pred);

# 06
pd.DataFrame({'isUSA': pred}).to_csv('./yemoonsaBigdata/res/003000000.csv', index=False);