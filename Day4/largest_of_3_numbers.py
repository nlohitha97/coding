#Lrgest of Three Numbers (Easy)
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

#time = o(1),space = O(1)