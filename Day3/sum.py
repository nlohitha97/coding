# Find the sum of digits of a number.
n=int(input("enter n:"))
sum=0
while n>0:
    num=n%10
    sum+=num
    n=n//10
print(f"the sum of digits of {n} is {sum}")
