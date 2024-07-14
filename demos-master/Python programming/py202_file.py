import os


def write_file(filename):
    if os.path.exists(f"{filename}"):
        print("File already exists")
    else:
        with open(filename, mode="w") as fw:            # will overrite existing file
            for l in range(1, 7):
                fw.write(f"line {l}\n")


def read_file(filename):
    with open(filename, mode="r") as fr:
        line = fr.read(10)      # reads 10 characters including \n
        print(line)
        print("-------")
        line = fr.read()       # reads the rest of the file
        print(line)


def read_file2(filename):
    with open(filename, mode="r") as fr:
        for line in fr:
            print(line, end="")


write_file("file1.txt")
read_file2("file1.txt")
