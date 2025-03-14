#write a program to find a sum of all the even numbers upto 100
# n = 0 #start
# sum = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum += i
# print(sum)

#Write a program to write first 20 numbers and their squared numbers
# n = 1
# for i in range(1, 21):
#     print(n, n * n)
#     n += 1

#write a program to find sum of first 10 odd numbers using while loop

# sum = 0
# n = 0
# while n <=20:
#     if n % 2 != 0:
#         sum += n
#     n += 1
# print("Sum of first 10 odd numbers is",sum)

#write a program to check a number is divisible by 5 and 7 , upto 100 numbers

# for i in range(1, 100):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)
        
#Write a program to create a billing system at supermarket
#use nested loop
# while True:
#     name = input("Enter customer name: ")
#     total = 0
#     while True:
#         print ("Enter the amount and quantities of items")
#         amount = float(input("Enter amount:"))
#         quantity = float(input("Enter quantity:"))
#         total += amount * quantity
#         repeat = input("Do you want to add more items? (yes/no): ")
#         if repeat == "no" or repeat == "No":
     
#             break
#     #print("-"*40)
#     print("Total amount to be paid by", name, "is", total)
#     print("*** Happy Shopping***")
    
#     repeat1 = input("do you want to go next customer? (yes/no). ")
#     if repeat1 == "no" or repeat1 == "No":
#         break

#Find the length of the line "India that is Bharat"
a = "India that is Bharat"
# print(len(a))
# b = len(a)
# print("the length of string is: " , b)

#Write a program to check how many times alphabet a is occurin "India that is Bharat"
print(a.count("a"))

#write a program to conver the whole string into lower and upper case
x = a.lower()
print(x)

y = a.upper()
print(y)

#Write a program to convert the following string into a title case
z = a.title()  #title means first letter capital
print(z)

#Write a program to find the index number of "Bharat"
print(a.index("Bharat"))

#write a pattern
# for i in range(1,6):  
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
    
# for i in range(1,6): #rows
#     for j in range(1, i+1): #columns
#         print(j, end = " ")
#     print()

# for i in range(1,6): #rows
#     for j in range(1, i+1): #columns
#         print(i, end = " ")
#     print()
    
# for i in range(1,6): #rows
#     for j in range(6, i, -1): #columns
#         print(j, end = " ")
#     print()
    
# for i in range(1,6): #rows
#     for j in range(6, i, -1): #columns
#         print(i, end = " ")
#     print()
    
# for i in range(1,6): #rows
#     for j in range(4, i, -1): #columns
#         print("", end = " ")
#     for k in range(1, i+1): #columns
#         print(k, end = " ")
#     print()
    
# for i in range(1,6): #rows
#     for j in range(5, i, -1): #columns
#         print("", end = " ")
#     for k in range(i): #columns
#         print("*", end = " ")
#     print()

# for i in range(1,6): #rows
#     for j in range(i, 0, -1): #columns
#         print(j, end = " ")
    
#     print()
    
# for i in range(1,6): #rows
#     for j in range(1, i+1): #columns
#         print("*", end = " ")
#     print()
# for i in range(5, 0, -1): #rows
#     for k in range(0, i-1): #columns
#         print("*", end = " ")
#     print()

for i in range(1,11): #rows
    for j in range(1,11): #columns
        print(i*j, end = "  ")
    print()
    
for i in range(1,11): #rows
    for j in range(1, i+1): #columns
        print(i*j, end = "  ")
    print()