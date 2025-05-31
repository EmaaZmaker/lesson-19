try:
    num1,num2=eval(input("enter two numbers seperated by commas"))
    result= num1 / num2
    print(result)
except ZeroDivisionError:
    print("this is zero division error")
except SyntaxError:
    print("comma missing,Please write numbers seperated by commas")
except NameError:
    print("please write a valid value")
else:
    print("no exception")
finally:
    print("I WILL GET EXECUTED NO MATTER WHAT")