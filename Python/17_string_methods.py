s = " hello world "

a = len(s)
print(a)

print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())

print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(s.find("world"))
print(s.replace("hello","hola"))

text = "apple,banana,orange"

print(text.split(","))
print(",".join(['apple','banana','orange']))

print(text.isalpha())
print(text.isalnum())
print(text.isdigit())
print(text.isspace())
