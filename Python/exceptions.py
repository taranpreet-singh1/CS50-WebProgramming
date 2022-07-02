import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.") 

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot didide by 0")
    sys.exit[(1)]
