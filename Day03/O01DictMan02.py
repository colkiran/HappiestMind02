
cities = ['blr', 'che', 'mum', 'hyd', 'del', 'kol']
print(f"cities :{cities}")
print(type(cities))

# convert the list into a dictionary by taking the list elements as keys of the dict
res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 23)
print(f"res2 :{res2}")

print("setdefault".center(40, "-"))
# add new key value pairs into the dict
player = {'name': 'sachin', 'runs': 45, 'oppn': 'Eng', 'venue': 'oval'}
print(f"player :{player}")
player.setdefault('gender', 'male')
player.setdefault('year', 2004)
player.setdefault('runs', 120)
player.setdefault('name', 'Tendulkar')
print(f"player :{player}")

# keys + values
print("{:*^40}".format("items"))
emp = {
    'emp1': {'empname': 'Jack', 'age': 28, 'desig': 'TL', 'dept': 'Finance', 'salary': 60000},
    'emp2': {'empname': 'Mike', 'age': 30, 'desig': 'BDE', 'dept': 'MKT', 'salary': 45000},
    'emp3': {'empname': 'Tim', 'age': 32, 'desig': 'SE', 'dept': 'IT', 'salary': 85000}
}

print(f"emp :{emp}")
print("-" * 40)
print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 40)
for ky, info in emp.items():
    print(ky)
    print("-----")
    for k, v in info.items():
        print(k, "=>", v)
    print("-"* 40)

print("pop".center(40, "-"))
player = {'name': 'sachin', 'runs': 45, 'oppn': 'Eng', 'venue': 'oval', 'gender': 'male', 'year': 2004}
print(f"player :{player}")

res = player.pop('venue')
print(f"res :{res}")

res = player.pop('gender')
print(f"res :{res}")

# res = player.pop('age')
print(f"player :{player}")

print("popitem".center(40, "-"))
player = {'name': 'sachin', 'runs': 45, 'oppn': 'Eng', 'venue': 'oval', 'gender': 'male', 'year': 2004}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")

print("update".center(40, "-"))
emp1 = {'empname': 'Jack', 'age': 28, 'desig': 'TL',  'salary': 60000}
emp2 =  {'empname': 'Mike', 'age': 30, 'desig': 'BDE', 'dept': 'MKT'}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 40)
emp1.update(emp2)
print(f"emp1 :{emp1}")
