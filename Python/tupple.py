# a = "apple", "banana", "cherry", 2, 3, 4.5
# print(a, type(a))

# b = "mango"
# print(b, type(b))

# c = "apple",
# print(c, type(c))

#Slicing of tupple
a =("apple", "banana", "cherry", 2, 3, 4.5)
# print(a[0:2])
# print(a[2:])
# print(a[0:4:1])
# print(a[::2])  #gap of 2
# print(a[::-1]) #reverse
# print(a[1::2])  #  gap of 2
#print(a[-1:-5:-1])
#print(a[2::-1])

#Iteration of tupple
#with for loop
# for i in a:
#     print(i)
    
#along with while loop
# i = 0
# while i < len(a):
#     print(a[i])
#     i = i + 1

#along with range and length in for loop
for i in range(len(a)):
    print(a[i])
