
# maketrans, translate
st = "hello world"
a = "helowrd"
b = "HELOWRD"                           # len(a) == len(b)
print(f"st :{st}")
resTbl = st.maketrans(a, b)             # returns a dictionary
print(f"resTbl :{resTbl}")
res = st.translate(resTbl)
print(f"res :{res}")