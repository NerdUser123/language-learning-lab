# q1

a = float(input("enter a num: "))

if(a < 0):
    print(" the number",a,"is negative")
elif(a > 0):
    print(" the number",a,"is positive")
else:
    print(" the number",a,"is zero")

# q2

b = int(input("enter your age"))

if( b > 18):
    print("you are eligible to vote")
elif(b < 18):
    print("you are not eligible to vote")
elif(b == 18):
    print("you can apply for voter id")
else:
    print("invalid")

# q3

c = int(input("enter the number"))

if(c%2 == 0):
    print("the number is even")
else:
    print("the number is odd")

# q4

d = int(input("enter the number 1 to 7 to print the the day"))

match d:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case 8:
        print("invalid")

# q5

e = float(input("enter num 1"))
f = float(input("enter num 2"))

g = (input("enter one of these (+ , - , * , /)"))

match g:
    case "+":
        print("ans:",e+f)
    case "-":
        print("ans:",e-f)
    case "*":
        print("ans:",e*f)
    case "/":
        print("ans:",e/f)

# q6

for i in range(1,11):
    print(i)

# q7

h = int(input("enter a num"))

for i in range(1,11):
    print(h,"*",i,"=",(h*i))

# q8

j = 0

for i in range (0,101):
    print(i)
    j += i
print(j)

# q9

for i in range (1,5):
    print("*"*i)

# q10

i=0
while(i<11):
    print(i)
    i = i + 1

# q11

k = input("enter your pass: ")
password = "abc"

while k != password:
    k = input("wrong pass, try again: ")

num = 123

# print(int(str(num)[::-1]))







