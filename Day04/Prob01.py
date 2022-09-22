
ch = "y"
FW = open("myfile.txt", "w")

while ch == "y":
    st = input("Enter the contents of the file :")
    FW.write(st + "\n")
    ch = input("Do you want to continue y / n ?")

FW.close()
