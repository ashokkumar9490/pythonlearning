dict1 = {1: "one", 2: "two"}
print(dict1)

print(dict1[1])     # key of an element

# # print(dict1[3]) # error

dict1[3] = "three"
print(dict1)
print(dict1[3])
dict1[3] = "four"       # modify the element value with this key
print(dict1[3])
dict1[3] = "three"
dict1[6] = "six"
dict1[5] = "five"
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

for k, v in dict1.items():      # destructuring
    print(f"{k} - {v}")

del (dict1[1])      # removed item having key as 1
print(dict1)

l1 = sorted(list(dict1), reverse=True)
print(l1)
