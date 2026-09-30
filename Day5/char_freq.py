# 9. Character Frequency (Easy)
s = input()
f = {}
for i in s:
    if i in f:
        f[i]+=1
    else:
        f[i] = 1
print(f)

# Time Complexity: O(n) | Space Complexity: O(k) where k is number of unique characters