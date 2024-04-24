# scikit-learn 데이터 전처리
# 01
from sklearn.preprocessing import LabelEncoder;

items = ['TV', '냉장고', '전자레인지', '컴퓨터', 'TV', '냉장고', '컴퓨터', '컴퓨터'];

encoder = LabelEncoder();
encoder.fit(items);
labels = encoder.transform(items);

print("인코딩 변환값: ", labels);
print("인코딩 클래스: ", encoder.classes_);

# 02
origins = encoder.inverse_transform([0, 1, 2, 3, 0, 1, 3, 3]);

print("디코딩 원본값: ", origins);

# 03
from sklearn.preprocessing import OneHotEncoder;

labels = labels.reshape(-1, 1);
oh_encoder = OneHotEncoder();
oh_encoder.fit(labels);
oh_labels = oh_encoder.transform(labels);

print("원-핫 인코딩 데이터");
print(oh_labels.toarray());
print("원-핫 인코딩 데이터 차원");
print(oh_labels.shape);

# 04
import pandas as pd;

item_df = pd.DataFrame({"item": items});
print(pd.get_dummies(item_df));

# 05
from sklearn.datasets import load_iris;
import pandas as pd;

iris = load_iris();
iris_data = iris.data;
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names);

print("feature들의 평균 값: \n", iris_df.mean());
print("feature들의 분산 값: \n", iris_df.var());

# 06
from sklearn.preprocessing import StandardScaler;

scaler = StandardScaler();
scaler.fit(iris_df);
iris_scaled = scaler.transform(iris_df);
iris_df_scaled = pd.DataFrame(data=iris_scaled, columns=iris.feature_names);

print("feature들의 평균 값: \n", iris_df_scaled.mean());
print("feature들의 분산 값: \n", iris_df_scaled.var());

# 07
from sklearn.preprocessing import MinMaxScaler;

scaler = MinMaxScaler();
scaler.fit(iris_df);
iris_scaled = scaler.transform(iris_df);
iris_df_scaled = pd.DataFrame(data=iris_scaled, columns=iris.feature_names);

print("feature들의 최소 값: \n", iris_df_scaled.min());
print("feature들의 최대 값: \n", iris_df_scaled.max());

# 08
import numpy as np;

train_array = np.arange(0, 11).reshape(-1, 1);
test_array = np.arange(0, 6).reshape(-1, 1);

scaler = MinMaxScaler();
scaler.fit(train_array);
train_scaled = scaler.transform(train_array);

print("원본 train_array 데이터: ", np.round(train_array.reshape(-1), 2));
print("Scaled train_array 데이터: ", np.round(train_scaled.reshape(-1), 2));

# scaler.fit(test_array
test_scaled = scaler.transform(test_array);

print("\n원본 test_array 데이터: ", np.round(test_array.reshape(-1), 2));
print("Scaled test_array 데이터: ", np.round(test_scaled.reshape(-1), 2));
