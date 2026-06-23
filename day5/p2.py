try:
    print("i am just started")
    print(10/2)
    print("i am try ,and done")
except ZeroDivisionError as zd:
    print(zd) 
else:
    print("Hi I am else mow alive because try is executed ")


try:
    print("i am just started")
    print(10/0)
    print("i am try ,and done")
except ZeroDivisionError as zd:
    print(zd) 
else:
    print("Hi I am else mow alive because try is executed ")


try:
    print("i am just started")
    print(10/0)
    print("i am try ,and done")
except ZeroDivisionError as zd:
    print(zd) 
else:
    print("Hi I am else mow alive because try is executed ")
finally:
    print("hello there i am finally, I am going to close")



