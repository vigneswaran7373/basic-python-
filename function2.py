def cse(*student):
    print(student)
cse("vignes","arun","sam",5)
"""arbitrary arguments"""
def line():
    print("-------------------------------------------------------------------------------------------")

line()
def message(name,age):
    print(name ,"age is",age)
message(age=18,name="vignes")
"""keyword arguments"""

line()
def biodata(**data):
    print(data)
biodata(name="ram",age=18,gender="male")
"""keyword and arbitrary arguments"""

line()
def user(name,city="salem"):
    print(name,"is from",city)
user("ram","salem")
user("sam")
"""default argument"""
line()
def tot(mark):
    return sum(mark)
print(tot([55,65,75,45,35]))
"""passing list argument"""

a=10.8
b=int(a)
print("float become int",b)
"""type casting"""
c=34
print(type(c))
"""find data type"""
g=233
h=233
print(id(g))
print(id(h))
"""find memory address for variable"""

a={10,2,34,55,78}
print(22 in a)
print(22 not in a)
"""membership operator"""
a=[1,2]
b=[1,2]
c=a
print(a is b)
print(a is c)
print(a is not c)
print(a is not b)
"""identity operator"""
z=45
x=66
print(a^b)
print(a|b)
print(a&b)
print(~a)
print(a>>2)
print(a<<2)
"""bitwise operator """