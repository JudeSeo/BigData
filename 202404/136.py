# 01
a = {1, 2, 3, 2, 1};
b = set([1, 2, 3, 2, 1]);
c = set("Python");

print(a);
print(b);
print(c);

# 02
a = set([1, 2, 3]);
b = list(a);
c = tuple(a);

print(a);
print(b);
print(b[0]);
print(c);
print(c[2]);

# 03
a = set([1, 2, 3, 4, 5]);
b = set([3, 4, 5, 6, 7]);
c = a & b;
d = a.intersection(b);

print(c);
print(d);

# 04
a = set([1, 2, 3, 4, 5]);
b = set([3, 4, 5, 6, 7]);
c = a | b;
d = a.union(b);

print(c);
print(d);

# 05
a = set([1, 2, 3, 4, 5]);
b = set([3, 4, 5, 6, 7]);
c = a - b;
d = a.difference(b);

print(c);
print(d);
