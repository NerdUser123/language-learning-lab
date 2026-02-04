student = {"name":'xyz', "age":18, "grade":'A'}
print(student)

print(student.keys())
print(student.values())
print(student.items())

student.pop('age')
print(student)

student.clear()
print(student)
