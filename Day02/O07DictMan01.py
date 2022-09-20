
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'name': 'sachin', 'runs': 125, 'oppn': 'Aus', 'vunue': 'Perth'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'rahul'), ('runs', 85), ('oppn', "Srilanka"), ('venue', 'gale')])
print(f"d3 :{d3}")

print("-" * 40)
d4 = dict(name='sehwag', runs=50, oppn='NZL', venue="Auckland")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
player = {'name': 'Sachin', 'runs': 85, 'oppn': 'WI', 'venue': 'Sabina Park'}
print(f"player :{player}")

print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")
print(f"Opponent :{player['oppn']}")

print("-" * 40)
for i in player:
    print(i, "=>", player[i])

print("-" * 40)
player['age'] = 32
player['year'] = 2002
player['runs'] = 120
player['venue'] = "Chinaswamy"

print(f"player :{player}")

print("-" * 40)
del player['venue']
del player['age']

print(f"player :{player}")

print("-" * 40)
print(player.get('name', "Invalid key, Please enter a key"))
print(player.get('venue', "Invalid key, Please enter a key"))

print("-" * 40)
print(dir(player))

print("keys".center(40, "-"))
player  = {'name': 'Sachin', 'runs': 120, 'oppn': 'WI', 'venue': 'Chinaswamy', 'age': 32, 'year': 2002}
print(f"player :{player}")

print("-" * 40)
k = player.keys()
print(k)
print(type(k))

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))
v = player.values()
print(f"v :{v}")
