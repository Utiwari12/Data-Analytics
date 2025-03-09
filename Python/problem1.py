#Write a program to get Fibonacci series of first 10 numbers
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
    


#Write a program to check if a number is prime or not

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
    
#Write a program to check if a number is palindrome of integers
# num = int(input("enter a number here: "))
# temporary = num
# reverse = 0
# while num > 0:
#     remainder = num % 10
#     reverse = reverse * 10 + remainder
#     num = num // 10
# if temporary == reverse:
#     print("It is a palindrome number")
# else:
#     print("It is not a palindrome number")


#Write a program to create an area calculator for different shapes
#area calculator
print("Area Calculator")
while True:
    
    print("""press 1 to get the area of square
    press 2 to get the area of rectangle
    press 3 to get the area of circle
    press 4 to get the area of triangle""")
    choice = int(input("Enter your choice number between 1-4 : "))
    if choice == 1:
        while True:
            side = float(input("Enter the side of square: "))
            area = side * side
            print("The area of square is: ", area)
            repeat = input("do you want to try again? ")
            if repeat == "yes":
                continue
            else:
                break
    elif choice == 2:
        length = float(input("Enter the length of rectangle: "))
        width = float(input("Enter the width of rectangle: "))
        area = length * width
        print("The area of rectangle is: ", area)
    elif choice == 3:
        radius = float(input("Enter the radius of circle: "))
        area = 3.14 * radius * radius
        print("The area of circle is: ", area)
    elif choice == 4:
        base = float(input("Enter the base of triangle: "))
        height = float(input("Enter the height of triangle: "))
        area = 0.5 * base * height
        print("The area of triangle is: ", area)