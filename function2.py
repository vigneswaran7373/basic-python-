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
