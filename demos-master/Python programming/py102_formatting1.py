pi = 3.141592
s = "value of PI"

print("%s is %f", (s, pi))

output = "{str} is {pival}"
print(output.format(str=s, pival=pi))

print("{0} is {1}".format(s, pi))

print(f"{s} is {pi}")
