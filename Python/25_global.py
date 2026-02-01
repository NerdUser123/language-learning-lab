def sum(a,b):
    c = a + b
    global z # global variable can be modified into the in the function
    z = 0
    print(z)
    return c


z = 10
print(sum(1,2))