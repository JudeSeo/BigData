# 01
a = True;

if a:
    print("가설은");
    print("사실이다.")
else:
    print("가설은");
    print("거짓이다.");

# 02
x = 3;
y = 7;

if x <= y:
    print("x가 y보다 작거나 같다.");
else:
    print("x가 y보다 크다.");

# 03
x = 3;
y = 7;

if x == y or x < y:
    print("x가 y보다 작거나 같다.");
else:
    print("x가 y보다 크다.");

# 04
x = 3;
y = [1, 2, 3, 4, 5];

if x in y:
    print("데이터가 존재한다");
else:
    print("데이터가 존재하지 않는다");

# 05
x = 3;
y = 7;

if x == y:
    print("x와 y는 같다.");
elif x < y:
    print("x가 y보다 작다.")
else:
    print("x가 y보다 크다.");
