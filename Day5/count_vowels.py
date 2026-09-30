#Count Vowels
n = input()
v ='aeiouAEIOU'
c =  0
for i in n:
    if i in v:
        c+=1
print(c)

#Time Complexity: O(n) | Space Complexity: O(1)
