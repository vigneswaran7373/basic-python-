try:
    a=10/0
except Exception :
    print("logic mistake")
    """try block"""
try:
    a=10/0
except Exception as e:
    print("logic mistake",e)
else:
    print("a value:",a)
    """try else block"""

try:
    a=10/25
except Exception as e:
    print("logic mistake",e)
else:
    print("a value:",a)
finally:
    print("thank you")
"""try expect else finally"""

try:
    print(a)
except NameError as e:
    print("a is not defined")
"""name error exception"""

try:
    a=int("joes")
except ValueError as e:
    print("please enter number only")
"""value exception"""

try:
    a=[10,20,30,40]
    print(a[10])
except IndexError as e:
    print("invalid index")
"""invalid index exception"""

try:
    f=open("text.txt")
except FileNotFoundError:
    print("file not found ")
else:
    print(f.read())
"""file not found exception"""

try:
    a=10/20
    b=[10,20,30,40]
    print(b[10])
except ZeroDivisionError:
    print("denominator can be zero")
except IndexError:
    print("invalid index")
"""handling multiple exception"""

print(dir(locals()["__builtins__"]))
print(len(dir(locals()["__builtins__"])))
"""list of exception type just know"""
