
"""
if the file exists then first delete the contents of the file and then writes into the file
if the file does not exist then creates a new file and writes into it
"""
FW = open("myfile.txt", "w")

st = input("Enter the contents of the file :")

FW.write(st)

FW.close()