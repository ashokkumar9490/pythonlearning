# t = (1, 2, 3, 4, 3, 4)
# print(t)
# print(type(t))
# t[0] = 10    # error - 'tuple' object does not support item assignment


student = ('John', 25,
           'Computer Science')

print(student)
print(student[0])

# student[0] = 'Jane' # error - 'tuple' object does not support item assignment
# student.append('Jane') # error - 'tuple' object has no attribute 'append'
# student.remove('John') # error - 'tuple' object has no attribute 'remove'

# Tuple packing and unpacking
a = 1
b = 2
c = 3
d = 4
t = a, b, c, d
print(t)
print(type(t))

a, b, c, d = t
print(a)
print(b)
print(c)
print(d)
