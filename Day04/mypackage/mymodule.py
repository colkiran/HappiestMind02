
guest = "Sachin Tendulkar"

sports = ['cricket', 'hockey', 'football', 'tennis', 'swimming']

runs = {'odi': 18680, 'test': 22500, 't20': 1200}

def greet(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.")

def addMe(x, y):
    return x + y

class Product:

    def __init__(self, prodname, price):                   # constructor
        self.prodname = prodname
        self.price = price

    def get_details(self):
        print(f"The product is {self.prodname}\nPrice is {self.price}")

