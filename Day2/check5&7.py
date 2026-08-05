# Check whether a number is divisible by both 5 and 11.
n=int(input("enter num: "))
if n%5==0 and n%11==0:
    print(f"{n} is divisible by both 5 and 11")
else:
    print(f"{n} is not divisible")
