# scikit-learn 내장 데이터 세트

# 01
from sklearn.datasets import load_iris;

iris = load_iris();
print("붓꽃 데이터세트 타입: ", type(iris));

keys = iris.keys();
print("붓꽃 데이터세트 키: ", keys);

# 02
print("feature_name: ");
print(iris.feature_names);
print("\ntarget_names");
print(iris.target_names);
print("\ndata");
print(iris.data);
print("\ntarget");
print(iris.target);
