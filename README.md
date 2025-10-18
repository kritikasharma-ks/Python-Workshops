# Notes for Python from w3schools

## Python Intro

File format: .py
How to check if Python is installed? python --version
Syntax to exit Python CLI: exit()

## Python Syntax

Indentation in Python is for readability only: False
```
print("Hello World")
if 5 > 2:
    print("YES")
```

## Python Comments

The # is for single line comments
The """ is for multi line comments

## Python Variables

1. legal names: start with letter, underscore. Contain caps, lowercase, numbers. No spaces or dashes.
2. illegal names: start with number, contain dash or space.

Variables are case-sensitive.

1. Pascal Case: MyVariableName
2. Snake Case: my_variable_name

Multiple variables:

```
x, y, z = "Orange", "Banana", "Cherry" # means that (x = "Orange", y = "Banana", z = "Cherry")
x = y = z = "Orange" # means that (x, y, z are all "Orange")
```

1. Lists --> mutable; can be modified
2. Tuples --> immutable; cannot be modified

Output variables:

1. Same types can be added in print statement ie. print(x + y) where x = "Hello " and y = "World" (both str)
2. Different types cannot be added, use comma for separation during printing or change type

```
a = "Hello"
b = "World"

print(a + b)

# the above prints out HelloWorld

print("Hello", "World)

# the above prints out Hello World
```

Global variable:

1. create variable outside function = global (can use inside and outside function)
2. create variable inside function = local (cannot use outside function)

global --> use this keyword if you want var to be global and not local
ie.
```
x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)
```
the above will print Python is fantastic both times

## Python Data Types

1. text: str() --> string value
2. numeric: int(), float(), complex() --> integer, float = decimals, complex = real and imaginary number
3. sequence: list, tuple, range
4. mapping: dict
5. set: set, frozenset
6. boolean: bool
7. binary: bytes, bytearray, memoryview
8. none: NoneType

