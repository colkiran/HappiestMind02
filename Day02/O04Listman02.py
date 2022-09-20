
print("append".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")

print("extend".center(40, "-"))
l2 = list(range(6, 11))
print(f"l2 :{l2}")
l2.extend([11, 12, 13])
l2.extend([14, 15, 16])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)
print(f"l1 :{l1}")

print("{:-^40}".format("pop"))
l2 = list(range(1, 11))
print(f"l2 :{l2}")

res = l2.pop(3)
print(f"res :{res}")
print(f"l2 :{l2}")

res = l2.pop(7)
print(f"res :{res}")
print(f"l2 :{l2}")

res = l2.pop()
print(f"res :{res}")
print(f"l2 :{l2}")

print("Remove".center(40, "-"))
l3 = [1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 3, 1, 2, 1, 1, 2, 2, 3]
print(f"l3 :{l3}")
l3.remove(1)
l3.remove(3)
print(f"l3 :{l3}")
# l3.remove(5)

while l3.count(1):
    l3.remove(1)

print(f"l3 : {l3}")

# while True:
#     try:
#         l3.remove(1)
#     except ValueError:
#         break

print("clear".center(40,"-"))
l1 = list(range(1, 11))
print(F"l1 before :{l1}")
l1.clear()

print(F"l1 after :{l1}")

