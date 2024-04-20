# 리스트

# 01
a = [1, 2, 3, 4, 5];
b = ['a', 'b', 'c'];
c = a * 2 + b;
d = len(c);

print(c);
print(d);

# 02
a = [1, 2, 3, 4, 5];

print(a);
print(a[0]);
print(a[1:4]);
print(a[-1]);
print(a[4]);
print(a[2:]);
print(a[2:5]);
print(a[:3]);
print(a[0:3]);

# 03
a = [1, 2, 3, ['a', 'b', 'c']];

print(a);
print(a[3]);
print(a[3][0]);
print(a[3][1:]);
print(a[3][:1]);

# 04
a = [1, 2, 3, 4, 5];
a[2] = 10;
del a[4];

print(a);

# 05
a = [1, 2, 3];
a.append(10)

print(a);

# 06
a = [1, 5, 2, 4, 3];
a.sort();

print(a);

# 07
a = [5, 4, 3, 2, 1];
b = a.index(3);
c = a.index(5);

print(b);
print(c);

# 08
a = [1, 2, 3];
a.insert(0, 10);

print(a)

# 09
a = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1];
a.remove(4);

print(a);

# 10
a = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1];
b = a.pop(1);

print(a);
print(b);

# 11
a = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1];
b = a.count(1);

print(b);
