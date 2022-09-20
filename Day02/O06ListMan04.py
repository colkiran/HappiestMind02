
"""
sort        -   sort will sort the original list
sorted      -   will return a copy of the sorted list
"""
# sort the list
l1 = [10, 5, 9, 2, 6, 8, 1, 4, 3, 7]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending order  :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending order :{res_desc}")

print("-" * 40)
l1 = [10, 'zebra', 'apple', 5, 'blue', 'yellow', 9, 'white', 'green',2, 'pink', 'maroon', 6, 'cat', 'violet', 8, 'dog', 'queen', 1, 'tango', 'hen', 4, 3, 7, 190, 1450, 28, 234, 2167]
print(f"l1 :{l1}")
res = sorted(l1, key=ascii)
print("-" * 40)
print(f"res :{res}")

print("-" * 40)
cities = ['kanyakumari', 'delhi', 'bangalore', 'ooty', 'mumbai', 'thiruvananthapuram', 'pune', 'vishakapatnam', 'hyderabad', 'mysore', 'madurai']

print(f"cities :{cities}")
print("-" * 40)
res_asc = sorted(cities, key=len)
print(f"Ascending order :{res_asc}")
print("-" * 40)
res_desc = sorted(cities, key=len, reverse=True)
print(f"Descending order :{res_desc}")

print("-" * 40)

print("-" * 40)
# sort these according to the calendar
from calendar import month_name
print(f"month_name :{month_name}")
print(f"month_name :{list(month_name)}")

print("-" * 40)
print("-" * 40)
lm = []
for month in list(month_name):
    # print(month[0:3].lower(), end=" ")
    lm.append(month[0:3].lower())

print(f"lm :{lm}")

print("-" * 40)
def monthIndex(mon):
    if mon in lm:
        return lm.index(mon)

print("jan :", monthIndex("jan"))
print("aug :", monthIndex("aug"))
print("mar :", monthIndex("mar"))
print("dec :", monthIndex("dec"))
print("sep :", monthIndex("sep"))

print("-" * 40)
months = ['dec', 'aug', 'apr', 'nov', 'feb', 'jan', 'oct', 'mar', 'may', 'jul', 'jun', 'sep']
print(f"months :{months}")

print("-" * 40)
print("-" * 40)
res_asc = sorted(months, key=monthIndex)
res_desc = sorted(months, key=monthIndex, reverse=True)

print(f"Ascending  :{res_asc}")
print("-" * 40)
print(f"Descending :{res_desc}")

print("reverse".center(40, "-"))
l1 = [10, 5, 4, 9, 8, 1, 7, 3, 2, 6]
print(f"l1 :{l1}")
print(list(reversed(l1)))
