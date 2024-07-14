# name = "sharad"
# print(f"Hello, {name:15}*")
# print(f"Hello, {name:<15}*")
# print(f"Hello, {name:>15}*")


yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes/(yes_votes+no_votes)
print(percentage)
print(f"*{yes_votes:<12}* YES votes *{percentage:<10.2%}*")
print(f"*{yes_votes:>12}* YES votes *{percentage:>10.2%}*")

# for x in range(1, 11):
#     print(f'{x:2d} {x*x:3d} {x*x*x:4d}')
