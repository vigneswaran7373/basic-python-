i=1
while(i<=10):
      print("odd no:",i)
      i=i+2
"""while loop"""
v=0
for v in range(0,11,2):
      print("even no:",v)
"""for loop"""

for i in range(5,-1,-1):
      for  j in range(i):
               print("*",end="")
      print("*")
"""nested for loop"""

for i in range(1,6):
       if(i==3):
         continue;
       print(i)
else:
       print("for loop completed")
"""for else loop"""
b=1
while(b<=5):
      if(b==4):
         break
      print(b)
      b=b+1
else:
      print("loop is no break")
"""while else loop"""
print(list(range(5)))
print(list(range(0,10,1)))
"""range statement"""