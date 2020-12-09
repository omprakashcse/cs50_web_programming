import sys
x=int(input("x: "))
y=int(input("y: "))

try:
    result=x/y
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    sys.exit(1)
print(f"{x}/{y}={result}")