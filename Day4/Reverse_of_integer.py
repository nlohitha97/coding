# Reverse an Integer (Easy)
n = int(input('n: '))
rev = 0
while n>0:
    d = n%10
    rev = rev*10+d
    n=n//10
print(rev)

#time = O(log n),space = O(1)