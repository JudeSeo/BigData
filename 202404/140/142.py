# 01
a = 0;

while a < 5:
    print("a값은 %s 입니다." % a);
    a = a + 1;

print("while문이 종료되었습니다.");

# 02
a = 0;
b = ['사과', '바나나', '토마토'];

while a < len(b):
    print("바구니에서 %s를 꺼냈습니다" % b[a]);
    a = a + 1;

print("바구니에 아무것도 남아있지 않습니다.");

# 04
a = 5;

while a > 0:
    print("a값은 %s 입니다." % a);
    a = a - 1;

    if a == 2:
        break;

print("while문이 종료되었습니다.");

# 04
a = 0;

while a < 10:
    a = a + 1;
    if a % 2 == 0:
        continue;
    print(a);
