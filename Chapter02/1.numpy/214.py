# numpy 배열 크기 변형
import numpy as np;

# 01
array1 = np.arange(12);
print("array1: \n", array1);

array2 = array1.reshape(3, 4);
print("array2: \n", array2);

array3 = array1.reshape(3, 4, order='F');
print("array3: \n", array3);

# 02
array1 = np.arange(10);
array2 = array1.reshape(-1, 5);

print(array2);
print("arrays2 dim: ", array2.ndim);
print("arrays2 shape: ", array2.shape);

# 03
array1 = np.arange(12);
array2 = array1.reshape(2, 3, 2, order='F');

print(array2);
print("arrays2 dim: ", array2.ndim);
print("arrays2 shape: ", array2.shape);

# 04
array3 = array2.flatten();
print(array3);
