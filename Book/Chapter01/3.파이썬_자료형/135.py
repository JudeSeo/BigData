# 딕셔너리(Dictionary) 자료형

# 01
a = {'name': 'John', 'age': 30, 'birth': [11, 8]};

print(a);
print(a['name']);
print(a['birth']);

# 02
a = {'name': 'John'};
a['age'] = 30;
a['house'] = 'apartment';
a['birth'] = [11, 8]
del a['house']

print(a);

# 03
a = {'name': 'John', 'name': 'Park'};

print(a);

# 04
a = {'name': 'John', 'age': 30, 'birth': [11, 8]};
b = a.keys();
c = list(a.keys());

print(b);
print(c);

# 05
a = {'name': 'John', 'age': 30, 'birth': [11, 8]};
b = a.values();
c = list(a.values());

print(b);
print(c);

# 06
a = {'name': 'John', 'age': 30, 'birth': [11, 8]};
b = a.items();
c = list(a.items());

print(b);
print(c);

# 07
a = {'name': 'John', 'age': 30, 'birth': [11, 8]};
b = a.get('name');
c = a['name'];
d = a.get('house');
e = a.get('house', 'No data');

print(b);
print(c);
print(d);
print(e);
