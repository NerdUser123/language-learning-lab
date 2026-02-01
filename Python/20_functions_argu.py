def add(a,b):
    x = a + b
    return x

print(add(1,2))

# default arguments

def add(a,b,c=0):
    x = a + b + c
    return x

print(add(1,2,3))
print(add(1,2))

# keyword arguement

def stu(name,age):
    print(f"name : {name}, age : {age}")

stu(age=20, name="bob")
stu("bob",10)