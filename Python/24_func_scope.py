def sum(a,b):
    # a,b,c are the local variable and cannot be accessed outside this function
    c = a + b
    return c

print(sum(4,6))

# and now the variable are outside the function they are accessible anywhere in the code

a = 0
b = 0
c = 0

print(a)
print(b)
print(c)