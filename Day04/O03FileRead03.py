
FL = open("Data.txt", "r")

st = FL.readlines()                     # will store all the lines in a list

for line in st:
    print(line)

FL.close()