
print("Conversions".center(40, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("The number {val} {val} {val}".format(val = 36))
print("The number {val} {val:f} {val:b}".format(val = 36))
print("The number {val:10} {val:f} {val:b}".format(val = 36))
print("The number {val:5} {val:f} {val:b}".format(val = 36))
print("The number {val:5} {val:f} {val:b}".format(val = 36564289201))

print("Alignment".center(40, "-"))
print("{num:15} Tendulkar".format(num="Sachin"))
print("{num:15} Tendulkar".format(num=3))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 40)
from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 40)
print("{:15} Tendulkar".format("Sachin"))           # left aligned
print("{:-<25}".format("Sachin"))
print("{:-^25}".format("Sachin"))
print("{:->25}".format("Sachin"))
print("{:015.2f}".format(pi))

print("-" * 40)
print("{0:$^20}{1:*^20}".format("Sachin", "Tendulkar"))

print("\n")
width = 50
price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print("-" * width)
print(header_fmt.format("Item", "Price"))
print("-" * width)

print(fmt.format("Apples", 0.4))
print(fmt.format("Pears", 0.5))
print(fmt.format("Cantloupes", 1.92))
print(fmt.format("Dried Apricot (16.oz))", 8))
print(fmt.format("Prunes (4 lbs)", 12))
print("-" * width)
