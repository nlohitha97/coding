#Palindrome Number (Easy)
n = int(input('n:'))
temp = n
rem = 0
while n>0:
    d = n%10
    rem = rem*10+d
    n = n//10
if temp == rem:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Complexity: Time O(d) | Space O(1)