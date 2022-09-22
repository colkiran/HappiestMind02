
"""
if the file exists then writes into the file without disturbing the previous contents
if the file does not exist then creates a new file and writes into it
"""
FA = open("myfile.txt", "a")

st = input("Enter the contents of the file :")
FA.write(st + "\n")

FA.close()