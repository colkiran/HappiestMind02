
from collections import namedtuple

nmdTpl = namedtuple("Product", "prodname prc cat qty")
prod = nmdTpl(prodname="Pepsi", prc = 80, cat="Baverage", qty = 15)
print(prod)

print("-" * 40)
print(f"Product Name :{prod.prodname}")
print(f"Price        :{prod.prc}")
print(f"Category     :{prod.cat}")
print(f"Quantity     :{prod.qty}")

# prod.prc = 120
