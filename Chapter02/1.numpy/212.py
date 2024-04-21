# numpy 배열 생성

# 01
import numpy as np;

# 02
a1 = np.array([1, 2, 3]);
print(a1);
print("array1 type: ", type(a1));
print("array1 shape: ", a1.shape);

a2 = np.array([[1, 2, 3], [4, 5, 6]]);
print(a2);
print("array2 type: ", type(a2));
print("array2 shape: ", a2.shape);

a3 = np.array([[1, 2, 3]]);
print(a3);
print("array3 type: ", type(a3));
print("array3 shape: ", a3.shape);

# 03
print("array1 dim: ", a1.ndim);
print("array2 dim: ", a2.ndim);
print("array3 dim: ", a3.ndim);

# 04
a = np.arange(20);
print(a);

# 05
a = np.arange(1, 20, 3);
print(a);
