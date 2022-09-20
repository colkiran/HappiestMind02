
print("count".center(40, "-"))
l1 = [1, 2, 3, 4,1 ,1 ,1, 2, 1, 2,1 ,1, 1, 2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 1, 2, 1, 2]
print(f"l1 :{l1}")

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")

print("index".center(40, "-"))
l1 = [1, 2, 3, 4, 1 ,1 ,1, 2, 1, 2, 1 ,1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 3]
print(f"l1 :{l1}")

pos = l1.index(3)
print(f"Position :{pos}")

pos = l1.index(3, l1.index(3) + 1 )
print(f"Position :{pos}")

pos = l1.index(3, l1.index(3, l1.index(3) + 1) + 1)
print(f"Position :{pos}")

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")
l2 = l1                 # shallow copy - it copies the address along with data
print(f"l2 before :{l2}")

l2.extend([6, 7, 8, 9])
print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("-" * 40)
l3 = [6, 7, 8, 9, 10]
print(f"l3 :{l3}")
l4 = l3.copy()
print(f"l4 :{l4}")

l4.append(11)
l4.append(12)
l4. append(13)
l3.append(11)
print(f"l4 :{l4}")
print(f"l3 :{l3}")

print("-" * 40)
l5 = [1, 2, 3, 4, [11, 22, 33, 44, 55], 5, 6, 7]
print(f"l5  before:{l5}")
l6 = l5.copy()                         # deep Copy
print(f"l6 before :{l6}")
print(l6[4].extend([10, 20, 30]))
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("-" * 40)
l7 = [1, 2, 3, [6, 7, 8, 9, 10], 4, 5]
print(f"l7 before :{l7}")
from copy import deepcopy
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

l8[3].extend([11, 12, 13])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")