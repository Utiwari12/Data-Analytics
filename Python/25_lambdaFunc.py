# a = lambda x, y: x + y
# print(a(2, 3))

# b = lambda x, y: x * y
# print(b(2, 3))

# c = lambda x, y: x - y
# print(c(2, 3))

# a = lambda b: b**2
# print(a(4))

# z = lambda a, b, c: (a+b)*c
# print(z(2, 3 , 4))

a = lambda x, y: x if x > y else y
print(a(2, 3))
print(a(6, 4))