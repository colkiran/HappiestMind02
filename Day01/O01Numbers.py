
a = 10
b = -10

print(f"a :{a}")            # interpolation
print(type(a))              # RTTI - runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 40)
c = 10.0
d = -10.0

print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 40)

e = 2e3
f = -2e3

print(f"e :{e}")
print(type(e))

print(f"f :{f}")
print(type(f))

print("-" * 40)

g = 10 + 4j
h = 10 - 4j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

x = 3 + 2.5
print(f"x :{x}")

print(type(x))

x = 1
y = 2.5
z = x + y

print(x, type(x))

print(y, type(y))
print(z , type(z))

print("Conversion".center(40, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")


print("Number system".center(40, "-"))
print(11)               # decimal number
print(0b11)             # binary
print(0b101)            # binary
print(0o11)             # octal
print(0o101)            # octal
print(0xe)              # hexa
print(0xa)              # hexa

print("Number system conversion".center(50, "-"))
a = 100
print(f'a :{a}')
print(f"bin(a) :{bin(a)}")
print(f"oct(a) :{oct(a)}")
print(f"hex(a) :{hex(a)}")




