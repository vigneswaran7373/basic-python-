file=open("python.txt","r")
print(file.read())
file.close()
"""read file"""

file=open("python.txt","r")
print("readline",file.readline())
print("readlines",file.readlines())
file.close()
"""read line and lines"""

file=open("python.txt","r")
for line in file:
    print(line)
file.close()
"""loop line by line read"""

file=open("python.txt","w")
file.write("hi i am vicky")
file.close()
file=open("python.txt","r")
print(file.read())
file.close()
"""write file"""

file=open("python.txt","a")
file.write(" from salem")
file.close()
file=open("python.txt","r")
print(file.read())
file.close()
"""append file"""

"""   i write comment line because this is delete 

file permanently in case i use this code previous code not run the file was delete
import os
file name delete
if os.remove("python.txt"):
    foldername delete
    os.remove("python.txt")
else:
    print("file not found")
delete file and folder""" 
