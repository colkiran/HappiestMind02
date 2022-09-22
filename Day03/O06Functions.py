
def greet():
    print("Greeting Mr.Sachin, Welcome to the event......")

def greetGst(gname):
    print(f"Greeting Mr.{gname}, Welcome to the event.......")

# city is a default variable, gname is a non-default variable
def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.......")


greet()
print("-" * 40)
greetGst("Sachin")
greetGst("Yuvraj")
print("-" * 40)
greetGstCty("Sachin")
greetGstCty("Sunil")
greetGstCty("Rahul", "Bangalore")

print("-" * 40)
def admsn(name, dob, qlf, gender, conno, adr, city):
    print(f"Name            :{name}")
    print(f"DOB             :{dob}")
    print(f"Qualification   :{qlf}")
    print(f"Gender          :{gender}")
    print(f"Contact No.     :{conno}")
    print(f"Address         :{adr}")
    print(f"City            :{city}")

# *args  - list
admsn("Jack", "12/10/1980", "12th",  "Male", "34345345", "MG Road Mumbai", "Mumbai")

# **kwargs - dictionary
admsn(adr = "indira nagar, chennai", qlf = 'MBA', conno="45575669", dob='10/05/1984', city="Chennai", name="slater", gender="Male")

# variable length args
print("-" * 40)
def multiplyAll(*numbers):          # it can accept more than one number
    print(numbers)
    prod = 1
    for number in numbers:
        prod *= number
    print(prod)

multiplyAll(1, 2, 3, 4, 5)

print("-" * 40)

def extractDetails(**details):
    print(details)
    for x in details:
        print(f"{x} => {details[x]}")

extractDetails(name="Sachin", runs=135, oppn="Srilanka", venue="Eden Gardens")

print("-" * 40)
# function return values
def multiplyMe(x, y):
    return x * y

print("%i * %i = %i" % (10, 20, multiplyMe(10, 20)))

print("-" * 40)

def fact(num):
    if num<=1:
        return 1
    else:
        return (num*fact(num-1))

n = 5
print(f"The factorial of {n} is :{fact(n)}")

print("-" * 40)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

iter = int(input("Enter the number of iterations :"))
print("Fibanocci Series")
for i in range(iter):
    print(fib(i), end=" ")
print()

print("-" * 40)
def arithmaticCal(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

print(arithmaticCal(20, 8))

print("-" * 40)
# doc strings
def fun():
    # this is a comment
    "this is a doc string"
    print("hello world")

fun()
print(fun.__doc__)                      # docstring

print("-" * 40)

def fun1(x, y):
    """
        fun1(x, y)

        if x and y are integers then fun1 returns the sum of the two numbers
        if x and y are strings then fun1 returns the concatenation of two string
        if x and y are of different datatypes then it returns an error
    """
    return x + y

print(fun1(30, 20))

help(fun1)
