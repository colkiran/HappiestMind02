
"""
1. arithmatic operators
2. comparison or relational
3. logical
4. bitwise
5. Ternary
"""


# Arithmatic Operator
# + , -, *, /, //, %

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

print("Augmentor".center(40, "-"))
# +=, -=, *=    -   ++, --,
x = 10
print(f"before x :{x}")
x += 5
print(f"after x :{x}")
x /= 3
print(f"after x :{x}")

print("Comparison Operator".center(40, "-"))
# == , >=, >, <=, <
a = 10
b = 15
print(f"a :{a}")
print(f"b :{b}")

print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")

print("logical operators".center(40, "-"))
print(1 == 1 and 2 == 2)
print(1 == 2 and 2 == 2)
print(1 == 2 and 2 == 1)
print(1 == 1 or 2 == 2)
print(1 == 2 or 2 == 2)
print(1 == 2 or 2 == 1)
print(not(1 == 2 or 2 == 1))
print(not(1 == 2 or 2 == 2))

print("-" * 40)
print(ord("A"))                     # integer representation of unicode characters
print(ord("Z"))

print(ord("a"))
print(ord("z"))

print("bitwise operators".center(40,"-"))
print(5 | 3)
print(5 & 3)
print(5 ^ 3)
print(5 << 1)
print(8 << 1)
print(5 << 2)
print(16 >> 1)

print(5 >> 1)
print(~0)           # 0000 => 1111
print(~5)           # 1010


# ternary operator
age = 12
print("Eligible" if age > 18 else "Not Eligible")

