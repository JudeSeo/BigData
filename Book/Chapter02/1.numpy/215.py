# numpy 배열 데이터 추출하기
import numpy as np;

# 01
array1 = np.arange(1, 10);
print("array1: ", array1);

value1 = array1[2];
value2 = array1[-2];

print(value1);
print(value2);

# 02
array1 = np.arange(1, 10);
array2 = array1.reshape(3, 3);
print("array2: \n", array2);

value1 = array2[0, 0];
value2 = array2[-1, -1];
value3 = array2[-1, -2];

print(value1);
print(value2);
print(value3);

# 03
array1 = np.arange(1, 10);
array2 = array1[0:3];
array3 = array1[:3];
array4 = array1[3:];

print(type(array2));
print(array2);
print(array3);
print(array4);

# 04
array1 = np.arange(1, 10);
array2 = array1.reshape(3, 3);
print("array2: \n", array2);

print("array2[0:2, 0:2]\n", array2[0:2, 0:2]);
print("array2[1:3, 0:3]\n", array2[1:3, 0:3]);
print("array2[:2, 1:]\n", array2[:2, 1:]);
print("array2[:2, 0]\n", array2[:2, 0]);
