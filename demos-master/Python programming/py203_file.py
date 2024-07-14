def write_file(filename):
    with open(filename, mode="r+") as fw:
        for l in range(4, 6):
            fw.write(f"line {l}\n")


""" 
if file1.txt contains 3 lines before writing function called - 
line 1
line 2
line 3

after opening in r+ mode will open in read and write mode,
writing will start from position 0

line 4
line 5
line 3
"""


def read_file(filename):
    with open(filename, mode="r") as fr:
        line = fr.readline()

        while line:
            print(line, end="")
            line = fr.readline()


write_file("file1.txt")
read_file("file1.txt")
