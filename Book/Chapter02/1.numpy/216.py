# numpy 선형대수 기본연산
import numpy as np;

# 01
array1 = np.array([[1, 2, 3], [4, 5, 6]]);
array2 = np.array([[7, 8], [9, 10], [11, 12]]);

dot_array = np.dot(array1, array2);
print(dot_array);

# 02
array1 = np.array([[1, 2, 3], [4, 5, 6]]);
transpose_array = np.transpose(array1);

print(transpose_array);
