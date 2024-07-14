letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
print(letters)
# ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
