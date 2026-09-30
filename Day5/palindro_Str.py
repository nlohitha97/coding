#  Palindrome String (Easy)
# n = input()
# s = n[::-1]
# if n==s:
#     print("yes")
# else:
#     print("no")

# # Time Complexity: O(n) | Space Complexity: O(n)

s = input("Enter a string: ")
i= 0
j = len(s) - 1

while i < j:
    if s[i] != s[j]:
        print("no")
        break
    i += 1
    j -= 1
else:
    print("yes")

# Time Complexity: O(n) | Space Complexity: O(1)
