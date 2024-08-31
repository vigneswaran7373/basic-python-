user={
    "name":"ram",
    "age":"18"
}
print(user)
print(user["name"])
print(user["age"])
print(user.values())
print(user.keys())
print(user.items())
for x in user.values():
    print(x)
if "age" in user:
    print("present")
user.update({"gender:male"})
print(user)
user["age"]=27
user.pop("gender")
user.clear()

"""dictionaries and function"""
user={
    "user1":{
        "name":"vignes",
        "age":"25",
    },
    "user2":{
        "name":"vasu",
        "age":"25",
    },

}
print(user)