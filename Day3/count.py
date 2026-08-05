# Count the number of digits in a number.
n=int(input("enter n:"))
count=0
if n==0:
    count=1
else:
    while n>0:
        count+=1
        n=n//10
print(count)
