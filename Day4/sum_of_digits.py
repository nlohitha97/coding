#3. Sum of Digits (Easy)
n = int(input('n: '))
s = 0
while n >0:
    d = n%10
    s = s+d
    n = n//10
print(s)

#time = O(log n),space = O(1)