#What is the output of the following code?
'''
x = 50
def fun1():
    x = 25
    print(x)

fun1() #This will output 25 as this will only call the variable x defined inside the function.
print(x) #This will output 50 as the variable x here was declared as a global variable.

x = 75
def myfunc():
    x = x + 1
    print(x)

myfunc() #This will output an error as the variable x is not defined in the function.
print(x)

print(bool(0),bool(3.14159),bool(-3),bool(1.0 + 1j))

print(type(0xFF))
'''