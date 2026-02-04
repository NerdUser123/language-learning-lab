# q1

l1 = ["apple","banana","cherry"]

print(l1)

print(l1[0])

l1[1] = 'orange'

print(l1)

print(len(l1))


# q2

l2 = [x for x in range(1,11)]
print(l2)

print(l2[0:3])
print(l2[-3:])

# q3

num = [5,2,9,1,7]

num.sort()
print(num)

num.append(10)
print(num)

# q4

t = (10,20)
print(t)

# q5

t1 = list(t)

t1[0] = 50

t2 = tuple(t1)

print(t2)

# q6

my_set = {1,2,3,3,4}

print(my_set)

# q7

my_set.add(5)
print(my_set)

my_set.remove(2)
print(my_set)


my_set.discard(4)
print(my_set)

# q8

a = {1,2,3}
b = {3,4,5}

print(a.union(b))

print(a.intersection(b))

print(a.difference(b))

# q9

stu = {"name":"jhon", "age":20, "grade":"A+"}

print(stu["name"])

stu["grade"] = "A"

print(stu)

stu["city"] = "delhi"

print(stu)


# q10

print(stu.keys())
print(stu.values())
print(stu.items())

# q11

ll = [1,1,2,3,4,4,6,7,8,9,9,9]

ls = set(ll)

print(ls)

# q12

dict1 = {"a":1,"b":2,"c":3}

print(max(dict1.values()))

# q13

dict3 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 3}

d3 = dict1 | dict2
print(d3)

