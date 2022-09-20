
# emulate C syntax, printf
format = "Welcome %s, what a %s player"
print(format)
values = ("Sachin", "superb")                   # tuples
print(values)
a = 10
b = "hello"
c = 150
print(a, b, c, sep=", ")

print("-" * 40)
print(format % values)
print("Welcome %s, what a %s player" % ("Sachin", "superb"))

print("-" * 40)
print("Welcome %s, your rating of %.3f, what a %s player" % ("Sachin", 4.2, "class"))

format = "Welcome %s, your rating of %.3f, what a %s player"
print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.298, "class"))
print(format % ("Sachin", 4.467565, "class"))
print(format % ("Sachin", 4.3321, "class"))

# emulate unix shell syntax
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
print(tmpl.substitute(name="Sachin", adj= "class"))

# format strings from python

print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))

# *args = list,  **kwargs => dictionary
print("Welcome {1}, what a {2} player for {0}".format("India", "Sachin", "class"))
print("Welcome {name}, what a {adj} player for {cty}".format(cty= "India", name= "Sachin", adj= "class"))
print("Welcome {name}, your rating of {rating:.2f}, what a {adj} player".format(name= "Sachin", rating = 4.58, adj = "class"))


print("-" * 40)
# interpolation
name = "Sachin"
print(f"Welcome {name}")

from math import pi, e
print(f"PI = {pi} and Euler's constant is {e}")

print("PI = {} and Eulers constant = {}".format(pi, e))
print("PI = {} and Eulers constant = {} and magic number = {magic}".format(pi, e, magic=40585))
print("PI = {0} and Eulers constant = {1} and magic number = {magic}".format(pi, e, magic=40585))

print("-" * 40)
full_name = ['Sachin', "Tendulkar"]
print("Mr. {name}".format(name=full_name))
print("Mr. {name[0]}".format(name=full_name))
print("Mr. {name[0]} {name[1]}".format(name=full_name))

print("-" * 40)
import math
print(__name__)                 # double underscore name  => dunder-name

print(math.__name__)
print("the {mod.__name__} module gives the value of pi = {mod.pi} and Eulers constant = {mod.e}".format(mod=math))

print("-" * 40)

class Student:

    def __init__(self):
        self.name = "Rahul"

print(Student.__name__)
st1 = Student()
print(st1.name)