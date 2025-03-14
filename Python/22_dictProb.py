# Write a python program to sort a dictionary by key
#d = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
# print(d)
# print(sorted(d))

# Write a python program to sort a dictionary by value
# d = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
# print(d)
# print(sorted(d.values()))

#Write a python program to remove a key from a dictionary
# d = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
# print(d)
# d.pop(2)
# print(d)

#Write a python program to print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys
# d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# print(d)

a = dict()
for i in range(1, 16):
    a[i] = i**2
print(a)

#Write a progam to multiply all the items in a dictionary
e =  {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
product = 1
for i in e:
    product = product * e[i]
print(product)