# def hello():
#     print("hello world")
# hello()

# def add(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
    #print(a+b, a-b, a*b, a/b)
#add(2,3)

#parameters
#arguments

# def add(a,b): # a and b are parameters
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     #print(a+b, a-b, a*b, a/b)
# add(12,10)  # 12 and 10 are arguments
# add(100, 20)

# def rect(length, breadth):
#     area = length*breadth
#     return area

# area = rect(10, 20)
# print(area)

# def square(side):
#     area = side*side
#     return area

# area = square(10)
# print(area)

# def hello(name):
#     print("hello, my name is", name)
# hello("Rahul")

# arbitary arguments
# def hello(*name):
#     print("hello, my name is", name[1])
#     print("hello, my name is", name[2])
#     print("hello, my name is", name[0])
    
# hello("Rahul", "Sohan", "Sharma")

#Return and Recursion 
# def hello():
#     return("hello world")
# print(hello())

# def add(a,b):
#     return(a+b)
# print(add(2,3))

#Recursive function means loop inside a function
# def hello():
#     print("hello world")
#     return hello()
# print(hello())

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))


