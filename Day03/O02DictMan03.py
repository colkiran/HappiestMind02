
emp1 =  {'empname': 'Jack', 'age': 28, 'desig': 'TL', 'dept': 'Finance', 'salary': 60000}
print(f"emp1  before :{emp1}")
emp1.clear()
print(f"emp1  after :{emp1}")

print("\n")
print("copy".center(40, "-"))
emp1 =  {'empname': 'Jack', 'age': 28, 'desig': 'TL', 'dept': 'Finance', 'salary': 60000}
print(f"emp1 before :{emp1}")
emp2 = emp1                         # shallow copy -> copies the address with the data
print(f"emp2 before :{emp2}")

print("-" * 40)
emp2['location'] = "Bangalore"
emp2['qlf'] = 'Mtech'
print(f"emp1 after :{emp1}")
print(f"emp2 after :{emp2}")

print("=" * 40)
emp3 = {'empname': 'Jack', 'age': 28, 'desig': 'TL', 'dept': 'Finance', 'salary': 60000}
print(f"emp3 before  :{emp3}")
emp4 = emp3.copy()
print(f"emp4 before :{emp4}")

print("-" * 40)
emp4['location'] = "Bangalore"
emp4['qlf'] = 'Mtech'
print(f"emp3 after :{emp3}")
print(f"emp4 after :{emp4}")

print("=" * 40)
emp5 = {'empname': 'Jack', 'age': 28, 'desig': {'dell': 'trainee', 'hp': 'FE', 'IBM': 'TL'}, 'dept': 'Finance', 'salary': 60000}
print(f"emp5 before :{emp5}")
emp6 = emp5.copy()
print(f"emp6 before :{emp6}")

print("-" * 40)
emp6['desig']['cisco'] = 'asst. MGR'
emp6['desig']['CGI'] = 'MGR'

print(f"emp5 after :{emp5}")
print(f"emp6 after :{emp6}")

print("=" * 40)
from copy import deepcopy
emp7 = {'empname': 'Jack', 'age': 28, 'desig': {'dell': 'trainee', 'hp': 'FE', 'IBM': 'TL'}, 'dept': 'Finance', 'salary': 60000}
print(f"emp7 before :{emp7}")
emp8 = deepcopy(emp7)
print(f"emp8 before :{emp8}")

print("-" * 40)
emp8['desig']['cisco'] = 'asst. MGR'
emp8['desig']['CGI'] = 'MGR'

print(f"emp8 after :{emp8}")
print(f"emp7 after :{emp7}")
