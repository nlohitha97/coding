#Check whether a year is a leap year.
n=int(input("enter year:"))
if n%4==0:
    print(f"{n}is leap year")
else:
    print(f"{n}is not a leap year")