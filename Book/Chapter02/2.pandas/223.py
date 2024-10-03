# 데이터프레임 생성하기
import pandas as pd;

# 01
d = [
    ['100', '강백호', 9.7],
    ['101', '송태섭', 8.9],
    ['102', '서태웅', 9.3],
    ['103', '채치수', 6.1]
]
df = pd.DataFrame(d, columns=['번호', '이름', '점수']);
print(df);

# 02
d = {
    '번호': ['100', '101', '102', '103'],
    '이름': ['강백호', '송태섭', '서태웅', '채치수'],
    '점수': [9.7, 8.9, 9.3, 6.1],
}

df = pd.DataFrame(d);
print(df);

# 03
housing_df = pd.read_csv("california_housing_train.csv");

print('housing 변수 type: ', type(housing_df));
print(housing_df);
