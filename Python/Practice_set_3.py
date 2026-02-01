# q1

name = "hello"

print(name[0])
print(name[4])
print(len(name))

# q2

s1 = "hello"
s2 = "world"

print(s1 +" "+ s2)
print(s1,s2)

# q3

str = "Python Programming"

print(str[0:7])
print(str[12:18])
print(str[0::2])

# q4

text = "text"

print(text[::-1])

# q5

s = " i love python programmign "

print(s.strip())
print(s.title())
print(s.count('o'))

# q6

s3 = "123abc"

print(s3.isalnum())

# q7

name1 = "john"
age = 18

print(f"my name is {name1} and i am {age} years old.")
print("my name is {} and i am {} years old.".format(name1,age))

# q8

sen = "coding in python is fun"

print(sen.replace('fun','awesome'))
print(sen.find('python'))
print(sen.upper())

# q9

vow = ['a','e','i','o','u']
c = 0

for i in sen:
    print(i)
    if( i in vow):
        c = c + 1

print(c)

# q10

a = input("enter you text to check if it is palindrome or not: ")

if (a == (a[::-1])):
    print("the string is palindrome")
    print("entered string: {}".format(a))
    print("reversed string: {}".format(a[::-1]))
else:
    print("the string is not palindrome")
    print("entered string: {}".format(a))
    print("reversed string: {}".format(a[::-1]))