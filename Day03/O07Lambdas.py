
# anonymous functions with a single line expression

def add(x, y):
    return x + y

a = add
res = a(10, 20)
print(f"res :{res}")

print("-" * 40)
b = lambda x, y: x + y
print(b(30, 12))

# map filter and reduce
# map will excute the given expression on each element of the list

l = list(range(1,11))
print(f"l :{l}" )

squares = list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")

# convert  => temp c - f pr f = c, currencies from rupees to dollar
months = ['dec', 'aug', 'apr', 'nov', 'feb', 'jan', 'oct', 'mar', 'may', 'jul', 'jun', 'sep']
print(f"months :{months}")

# sort it using lambda
from calendar import month_name

print(list(month_name))

sorted_month = sorted(months, key = list(map(lambda m: m[0:3].lower(), list(month_name))).index)
print(sorted_month)

# filter
# expression => t / f
print("-" * 40)
l = list(range(1, 25))
print(f"l :{l}")

res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

print("-" * 40)
sentence  = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")
res = list(filter(lambda word: word != 'the', sentence.split()))
print(f"res :{res}")

# reduce - functools
print("-" * 40)
from functools import reduce
l = [8, 3, 7, 2, 9, 4, 5, 10, 6, 1]
print(f"l :{l}")

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

print("-" * 40)

res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")





