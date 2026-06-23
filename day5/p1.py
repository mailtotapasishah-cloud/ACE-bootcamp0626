try:
    print(10/0)
except ZeroDivisionError:
    print("Dividing with zero (0) is not allowed") 

try:
    print(10/0)
except ZeroDivisionError as zd:
    print(zd) 

