#Write a function to find maximum of 3 numbers
# def max(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# print(max(10, 20, 3))

#Write a function to find minimum of 3 numbers
# def min(a, b, c):
#     if a < b and a < c:
#         return a
#     elif b < a and b < c:
#         return b
#     else:
#         return c
#print(min(10, 20, 3))

#Write a program to create and display a list where the values are square of numbers between 1 and 30 (both included).
# a = []
# for i in range(1, 31):
#     a.append(i**2)
# print(a)

#Write a program that takes a number as a parameter and check if the number is prime or not

# num = int(input("enter a number here: "))

# if num <=1:
#     print(" It is not prime")
    
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("It is not prime number")
#             break
#     else:
#         print("It is prime number")

#Write a program to find the sum of all the numbers in a list
# a = [1, 2, 3, 4, 5]
# sum = 0
# for i in a:
#     sum = sum +i
# print(sum)

# sum = 0
# n = int(input("enter a number here: "))
# for i in range(1, n+1):
#     sum = sum + i
# print(sum)

#Write a program to find the average of all the numbers in a list
# sum = 0
# n = int(input("enter a number here: "))
# for i in range(1, n+1):
#     sum = sum + i
# print(sum/n)

#Write a program to solve the Fibonacci series of first 10 numbers
# a = 0
# b = 1
# n = int(input("enter a number here:"))
# if n == 1:
#     print(1)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a + b
#         print(c)
#         a = b
#         b = c
        
#Write a program to solve the Fibonacci series using recursion method
a = 0
b = 1
n = int(input("enter a number here:"))
if n == 1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c = a + b
        print(c)
        a = b
        b = c