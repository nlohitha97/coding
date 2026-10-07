try:
    num1 = 10
    num2 = 0
    # res = num1//num2
    # print(res)
    # lst = [1,2,3]
    # print(lst[4])
    a = int(input("Enter the number:"))
    print("user input: ",a)
except ZeroDivisionError:
    print(f"Error!,cannot divide by zero")
except IndexError:
    print(f"Error! index out of range")
except Exception:
    print(f"Invalid input enter only integer values")
finally:
    print("Execution completed")
    