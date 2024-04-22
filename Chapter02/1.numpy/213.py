# numpy 배열 초기화
import numpy as np;

# 01
zero_a = np.zeros((2, 5));
one_a = np.ones((3, 4));

print(zero_a);
print(one_a);

# 02
zero_b = np.zeros_like(one_a);
print(zero_b);

# 03
one_b = np.ones_like(zero_a);
print(one_b);

# 04
full_a = np.full((4, 3), 9);
random_a = np.random.random((3, 4));

print(full_a);
print(random_a);

# 05
eye_a = np.eye(4);
print(eye_a);
