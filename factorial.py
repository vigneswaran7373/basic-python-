def factorial(x):
    if x==1:
     return 1
    else:
       return(x*factorial(x-1))
n=int(input("enter the factorial number"))
print("factorial value",factorial(n))
"""factorial in python"""
def line():
   print("----------------------------------------------------------------------------------------------------")
line()
c=lambda a,b:a+b
print("use lambda function",c(10,20))
c=lambda a:a+50
print("use lambda function",c(10))
"""lambda function"""
line()
def add(x):
   pass 
add(5)
"""pass function"""
line()
