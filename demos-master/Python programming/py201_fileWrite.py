fw = open("file1.txt", mode="w")    # overrite the file
for l in range(1, 6):
    fw.write(f"line {l}\n")

fw.close()
