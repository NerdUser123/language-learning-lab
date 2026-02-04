import math
import requests
# q1

def greet():
    print("hello, python learner")

greet()

# q2

def square(num):
    return num*num

print(square(4))

# q3

def full_name(first,last):
    return f"{first} {last}"

print(full_name("jhon","doe"))

# q4

def area(x,y=10):
    return x*y

print(area(10))
print(area(10,20))

# q5

sum = lambda x,y : x+y
print(sum(10,20))

# q6

sqol = lambda x : x*x
l = [1,2,3,4,5]

print(list(map(sqol,l)))

# q7

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# q8

def sum_of_digit(n):
    if n == 0:
        return 0
    
    return n%10 + sum_of_digit(n//10)

print(sum_of_digit(123))

#  q9

print(math.sqrt(144))

print(math.sin(math.radians(90)))

# q10

a = requests.get("https://api.github.com")
print(a.json())

# q11

def increment():
    a = 0
    a += 1
    print(a)

increment()

# q12

def fib(z):
    if z == 0:
        return 0
    elif z == 1:
        return 1
    return fib(z-1) + fib(z-2)


print(fib(5))
