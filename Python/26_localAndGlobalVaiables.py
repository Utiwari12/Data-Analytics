#Local Variables

x = 24
print("The first value of x is",x)

def hello():
    x = 30
    return x
print(hello())

print("The local value of x is",x)

#Global Variables
x = 24
print("The first value of x is",x)
def hello():
    global x
    x = 30
    return x
print(hello())

print("The global value of x is", x)