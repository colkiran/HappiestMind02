
import sys
sys.path.append("C:/Delhi")

for path in sys.path:
    print(path)

from gurgaon.mymodule import Product

p1 = Product("Kit Kat", 45)
p1.get_details()


