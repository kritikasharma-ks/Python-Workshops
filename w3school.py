"""
Hands on exercises from tutorials 
"""

# Python Variables:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print("Different types:", x, y, z, sep="\n")
print("Classifying types:", type(x), type(y), type(z), sep="\n")

# Unpacking List:
fruits = ["Banana", "Orange", "Cherry"]
x, y, z = fruits
print ("Unpacking List:", x, y, z, sep="\n")

# Global Variables:
x = "awesome" #global var

def myfunc():
    x = "fantastic" #local var
    print("Python is " + x) #overrides "awesome" with "fantastic"

myfunc() #calls function defined with local var inside it

print("Python is " + x) #considers global var, not local

# Global Key Word:

x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

# Data Types:

print("\n" + "Data Types")
data1 = "Hello World"
data2 = 20
data3 = 20.5
data4 = 1j
data5 = ["apple", "banana", "cherry"]
data6 = ("apple", "banana", "cherry")
data7 = range(6)
data8 = {"name": "John", "age": 36}
data9 = {"apple", "banana", "cherry"}
data10 = frozenset({"apple", "banana", "cherry"})
data11 = True
data12 = b"Hello"
data13 = bytearray(5)
data14 = memoryview(bytes(5))
data15 = None

for i in range(1,16):
    values = eval("data" + str(i))
    print(f"data{i}: {values} ({type(values)})")

