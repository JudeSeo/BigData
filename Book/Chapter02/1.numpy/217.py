# numpy 기술통계
import numpy as np;

# 01
x = np.array([18, 5, 10, 23, 19, -8, 10, 0, 0, 5, 2, 15, 8,
              2, 5, 4, 15, -1, 4, -7, -24, 7, 9, -6, 23, -13]);

print(len(x));  # 예제에는 그냥 len(x)로 나와있으나, 출력이 안보이는 관계로 print 추가

# 02
print(np.mean(x));  # 평균
print(np.var(x));  # 분산
print(np.std(x));  # 표준편차

# 03
print(np.max(x));  # 최댓값
print(np.min(x));  # 최솟값
print(np.median(x));  # 중앙값

# 04
print(np.percentile(x, 25));  # 사분위수
print(np.percentile(x, 50));  # 사분위수
print(np.percentile(x, 75));  # 사분위수
