def add(a,b):
    c=a+b                                  
    return c
a=int(input("enter the number 1"))
b=int(input("enter the number 2"))
x=add(a,b)
print("output is:",x)
"""return type with argument"""

def add():
    a=int(input("enter the number 1"))
    b=int(input("enter the number 2"))
    c=a+b
    return c
x=add()
print("output is:",x)
"""return type with out argument"""

def add():
    a=int(input("enter the number 1"))
    b=int(input("enter the number 2"))
    c=a+b
    print("the out put is:",c)
add()
"""no return type with out argument"""

def add(a,b):
    c=a+b
    print("the out put is:",c)
a=int(input("enter the number 1"))
b=int(input("enter the number 2"))
add(a,b)
"""no return type with argument"""

    