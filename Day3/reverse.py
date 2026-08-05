# Reverse a number.
# approach 1
n=int(input("enter n:"))
rev = int(str(n)[::-1])
print(f"Reversed number: {rev}")

# approach 2
num=eval(input("enter n:"))
r=0
while num>0:
    digit = num%10
    r=r*10+digit
    num=num//10
print(f"Reversed number: {r}")  

# approach 3
n = int(input("enter n:"))
original = n
rev = 0
num_digits = len(str(n))   # find how many digits n has

for i in range(num_digits):
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(f"Reversed number: {rev}")