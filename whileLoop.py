# n =0
# while n<=10:
#     print(n)
#     #n +=1
#     n +=2

#multiplication table
# n=1
# a = int(input("enter a number here: "))
# while n<=10:
#     print(a,"x",n,"=",a*n)
#     #n +=1
#     n +=2 #for odd numbers

# while True:
#     #print("hello")
    
#  num1 = int(input("enter a number here: "))
#  num2 = int(input("enter a number here: "))
#  result = num1 + num2
#  print(result)
#  repeat = input("do you want to stop? ")
#  if repeat == "yes":
#      break  #break means stop

#Nested loop means a loop inside a loop

# for i in range(1,4):  #counting number of rows
#     for j in range(1,11): #counting number of columns
#         #print(j)
#         print(j, end=" ")
#     print()

#print a pattern for 5 rows and 5 columns
# for i in range(1,6): #counting number of rows
#     for j in range(1, i+1):  #counting number of columns
#         print(j, end= " ")  # horizontal print
#     print()

#Conditional loop
# for i in range(1,7):
#     if i == 3:
#         print("add this song is favourite")
#     else:
#         print(i)

# print all the numbers which are divisible by 8 and 12 between 1 to 100
# for i in range(1, 101):
#     if i% 8 == 0 and i% 12 == 0:
#         print(i)

# n = 1 #start from 1

# while n <=10:
#     if n == 3:
#         print("add this favourite")
#     else:
#         print(n)
#     n += 1

#continue and break statements
# for i in range(1, 11):
#     if i == 5:
#         continue # skip 5
#     else:
#        print(i)

for i in range(1,11):
    if i == 6:
        break  #stop the loop
    else:
        print(i)


 