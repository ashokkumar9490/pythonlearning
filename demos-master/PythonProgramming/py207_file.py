some_bytes = b'\xC3\xA9'


with open("fileb.bin", "wb") as binary_file:

    # Write bytes to file
    binary_file.write(some_bytes)


# Opening the binary file in binary mode as rb(read binary)
f = open("fileb.bin", mode="rb")

# Reading file data with read() method
data = f.read()

# Knowing the Type of our data
print(type(data))

# Printing our byte sequenced data
print(data)
