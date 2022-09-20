
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.2, 8.1, 9.5, True, False, 10 + 0j,  11 - 2j]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 6))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
# cannot insert new element into the list
l1 = list(range(1, 11))
print(f"l1 :{l1}")
l1[4] = 45
print(f"l1 :{l1}")

print("-" * 40)
l2 = list(range(10, 101, 10))
print(f"l2 :{l2}")
print(f"l2[3] :{l2[3]}")
print(f'l2[-1] :{l2[-1]}')
for i in l2:
    print(i, end= " ")
print()

for i in range(0, len(l2)):
    print(l2[i], end=" ")
print()

print("-" * 40)
print(f"l2 :{l2}")
del l2[2]
del l2[-1]
del l2[-2]
print(f"l2 :{l2}")

# unpacking
print("-" * 40)
values = list(range(10, 40, 10))
print(f"values :{values}")
a, b, c = values                        #unpack the list
print(a, b ,c ,sep=", ")

values = list(range(10, 101, 10))
print(f"values :{values}")
a, b, *c = values                       # * before a variable, that var can accept more                                              than one value
print(a, b ,c ,sep=", ")

print("-" * 40)
a, *b, c = values
print(a, b ,c ,sep=", ")

print("-" * 40)
*a, b, c = values
print(a, b ,c ,sep=", ")

print("-" * 40)
l1 = [1, 2, 3]
l2 = [3, 4, 5]
l3 = [l1, l2]
print(len(l3))
print(f"l3 :{l3}")

print("-" * 40)
l4 = [*l1, *l2]                 # unpack the list
print(len(l4))
print(f"l4 :{l4}")

print("-" * 40)
l5 = l1 * 2
print(len(l5))
print(f"l5 :{l5}")

print("-" * 40)
l6 = l1 + l2
print(len(l6))
print(f"l6 :{l6}")

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# no of iterations 5 => 5, 4, 3, 2, 1:    8 => 8, 7, 6, 5, 4, 3, 2, 1

# l2 = [1, 2, 3, 4, [10, 20, 30, 40, 50, 60, 70], 6, 7, 8, 9, 10]
# write a code that will reverse internal list

print("-" * 40)
print(dir(l1))
