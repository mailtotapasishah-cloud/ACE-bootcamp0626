try:
    a=int(input("Enter First value:"))
    b=int(input("Enter Second value:"))
    print("I a just started")
    if(b%2==0):
        raise Exception
    else:
        print(a/b)
except ZeroDivisionError as zd:
    print(zd)
except Exception as e:
    print("Division by evens are not allowed")
else:
    print("Hi I am else mow alive because try is executed ")
finally:
    print("hello there i am finally, I am going to close")
