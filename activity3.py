valid=False
while not valid:
    try:
        n=int(input("enter number"))
        while n % 2==0:
            print("bye")
        valid=True
    except ValueError:
        print("please enter a   v a l i d  number")