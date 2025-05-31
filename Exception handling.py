try:
    number=int(input("enter the number"))
    print(number)
except ValueError as ex:
    print("exception is",ex)
