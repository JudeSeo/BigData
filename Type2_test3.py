# 2024-06-22
import pandas as pd
#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/x_test.csv")


display(x_train.head())
display(y_train.head())

# drop
drop_col=['ID', 'Driving_License', 'id'];
x_train_drop = x_train.drop(columns=drop_col);
x_test_drop = x_test.drop(columns=drop_col);

# dummy, y
x_train_dummies = pd.get_dummies(x_train_drop)
y=y_train['Response'];

x_test_dummies = pd.get_dummies(x_test_drop);
x_test_dummies = x_test_dummies[x_train_dummies.columns];

# rf
from sklearn.ensemble import RandomForestClassifier;
from sklearn.model_selection import train_test_split;

X_train, X_validation, Y_train, Y_validation = train_test_split(x_train_dummies, y, test_size=0.33, random_state=42,stratify=y);
rf = RandomForestClassifier(random_state=23);
rf.fit(X_train, Y_train);

# metrics
from sklearn.metrics import f1_score, accuracy_score,  precision_score, recall_score, roc_auc_score

predict_train_label = rf.predict(X_train);
predict_train_proba = rf.predict_proba(X_train)[:,1];

predict_validation_label = rf.predict(X_validation);
predict_validation_proba = rf.predict_proba(X_validation)[:,1];

print('train accuracy :', accuracy_score(Y_train,predict_train_label))
print('validation accuracy :', accuracy_score(Y_validation,predict_validation_label))
print('\n')
print('train f1_score :', f1_score(Y_train,predict_train_label))
print('validation f1_score :', f1_score(Y_validation,predict_validation_label))
print('\n')
print('train recall_score :', recall_score(Y_train,predict_train_label))
print('validation recall_score :', recall_score(Y_validation,predict_validation_label))
print('\n')
print('train precision_score :', precision_score(Y_train,predict_train_label))
print('validation precision_score :', precision_score(Y_validation,predict_validation_label))
print('\n')
print('train auc :', roc_auc_score(Y_train,predict_train_proba))
print('validation auc :', roc_auc_score(Y_validation,predict_validation_proba))


predict_test_label = rf.predict(x_test_dummies);
predict_test_proba = rf.predict_proba(x_test_dummies)[:,1];

pd.DataFrame({'ID':x_test.ID, 'Response':predict_test_label}).to_csv('aaa.csv', index=False);