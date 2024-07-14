# squares = []
# for x in range(1, 11):  # 1-10
#     squares.append(x**2)


# print(squares)
# print(x)


squares = list(map(lambda y: y**2, range(1, 11)))
print(type(squares))
print(squares)
# print(y)   # not available
