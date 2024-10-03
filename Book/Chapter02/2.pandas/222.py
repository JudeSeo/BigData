# 시리즈와 데이터프레임 이해하기

# 01
import pandas as pd;

# 02
s = pd.Series([1, 3, 5, 6, 8]);

print(s);
print(s.index);
print(s.values);

# 03
v = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
i = ['첫째행', '둘째행', '셋째행'];
c = ['컬럼1', '컬럼2', '컬럼3'];

df = pd.DataFrame(v, index=i, columns=c);
print(df);
