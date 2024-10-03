# scikit-learn 머신러닝 만들어보기

# 01
import pandas as pd
from sklearn.datasets import load_iris;

iris = load_iris();

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['label'] = iris.target;
print(iris_df.head(3));

# 02
from sklearn.model_selection import train_test_split;

iris_data = iris.data;
iris_label = iris.target;

x_train, x_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.2, random_state=11);

print("train dataset");
print("x_train dataset: ", len(x_train));
print("y_train dataset: ", len(y_train));
print("\ntest dataset");
print("x_test dataset: ", len(x_test));
print("y_test dataset: ", len(y_test));

# 03
from sklearn.tree import DecisionTreeClassifier;

dt_clf = DecisionTreeClassifier(random_state=11);
dt_clf.fit(x_train, y_train);
print(dt_clf);

# 04
from sklearn.metrics import accuracy_score;

pred = dt_clf.predict(x_test);
ac_score = accuracy_score(y_test, pred);
print("예측 정확도: ", ac_score);
