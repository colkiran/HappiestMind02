
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"l1 :{l1}")
# reverse the list
# n = int(input("Enter the iteration :"))
n = 7
for i in range(n-1, -1, -1):
    print(l1[i], end= " ")

print("-" * 40)
l2 = [1, 2, 3, 4, [10, 20, 30, 40, 50, 60, 70], 6, 7, 8, 9, 10]
# write a code that will reverse internal list
print(f"l2 :{l2}")
l3= []
for i in l2:
    if (isinstance(i, list)):
        for n in range(len(i)-1, -1, -1):
            # print(i[n], end=" ")
            l3.append(i[n])

print(l3)

