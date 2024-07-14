def write_file(filename):
    with open(filename, mode="w") as fw:
        for l in range(1, 3):
            fw.write(f"line {l}\n")


def read_file(filename):
    with open(filename, mode="r") as fr:
        for line in fr:
            print(line, end="")


write_file("file1.txt")
read_file("file1.txt")
