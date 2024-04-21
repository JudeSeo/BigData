# 문자열(String) 자료형

# 01
a = "Hello World";
b = "Hello Python's World";
c = '"Hello World" he says';
d = "Hello World\nLife is good";

print(a);
print(b);
print(c);
print(d);

# 02
a = "Python";
b = " ";
c = "is good";

print(a + b + c);

# 03
a = "Python";

print(a * 3);

# 04
a = "Life is short, Python is valuable";
b = len(a);

print(b);

# 05
a = "Life is short, Python is valuable";
b = a[0];
c = a[10];
d = a[-8];
e = a[-1];

print(b + c + d + e);

# 06
a = "Life is short, Python is valuable";
b = a[:4];
c = a[4:8];
d = a[25:];

print(b + c + d);

# 07
a = "apple";
b = a.count('p');

print(b);

# 08
a = "apple";
b = a.find('p');

print(b);

# 09
a = "apple";
b = ','.join(a);

print(b);

# 10
a = "apple";
b = a.upper();
c = b.lower();

print(b);
print(c);

# 11
a = " apple";
b = a.lstrip();
c = a.rstrip();
d = a.strip();

print(b);
print(c);
print(d);

# 12
a = "Life is good";
b = a.replace("Life", "Python");

print(b);

# 13
a = "Life is short, Python is valuable";
b = a.split();
c = a.split(',');

print(b);
print(c);
