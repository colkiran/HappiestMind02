
st = "hello world"
print(f"st :{st}")

print("-" * 40)
print(f"st[0] :{st[0]}")                    # strings are stored like lists
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 40)
#slicing
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

print("-" * 40)
#reverse indexing
print(f"st[-1]  :{st[-1]}")
print(f"st[-5]  :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 40)
# slicing
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

# strings are immutable
# print("-" * 40)
# print(f"st :{st}")
# print(f"st[6] :{st[6]}")
# st[6] = "W"
print("-" * 40)
print(dir(st))

st = "hello world"
st1 = "the quick brown fox jumps over the lazy dog"

# find
print("find".center(40, "-"))
pos = st.find("l")
print(f"position :{pos}")
pos = st.find("l", st.find("l") + 1)
print(f"position :{pos}")
pos = st.find("l", st.find("l", st.find("l") + 1) + 1)
print(f"position :{pos}")

print("-" * 40)
print(f"st1 :{st1}")
pos = st1.find("the")
print(f"1st position of 'the' :{pos}")
pos = st1.find("the", st1.find("the") + 1)
print(f"2nd position of 'the' :{pos}")

print("replace".center(40, "-"))
print(f"st :{st}")
res = st.replace("l", "L")
print(f"res :{res}")
res = st.replace("l", "L", 1)
print(f"res :{res}")

print("-" * 40)
print(f"st1 :{st1}")
res = st1.replace("the", "The")
print(f"res :{res}")
res = st1.replace("the", "The", 1)
print(f"res :{res}")
