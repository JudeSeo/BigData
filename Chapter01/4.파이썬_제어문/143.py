# for문

# 01
a = ['사과', '바나나', '토마토'];

for i in a:
    print(i);

# 02
a = [90, 25, 67, 45, 80];
b = sum(a) / len(a);

for i in a:
    if i > b:
        print("%d 는(은) 평균보다 크다." % i);
    else:
        print("%d 는(은) 평균보다 작거나 같다." % i);

# 03
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=' ');
    print(' ')

# 04
a = [1, 2, 3, 4];
result = [];

for i in a:
    result.insert(0, i * 10);

print(result);
