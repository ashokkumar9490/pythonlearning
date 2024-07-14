f = open("foo.txt")  # Returns a file object default text file

# file_content = f.read()  # Reads the entire file content
# print(file_content)

# # read file using while loop

# line = f.readline()  # Invokes readline() method on file
# while line:
#     print(line, end='')
#     # print(line)                 # 11\n\r
#     line = f.readline()

line_no = 1
for line in f:
    print(f"{line_no} - {line}", end='')
    line_no += 1


f.close()


# # Read file using with statement
with open("foo.txt") as f:
    for line in f:
        print(line, end='')
