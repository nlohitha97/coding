#Find the largest of three numbers.
a,b,c = map(int,input("enter:").split())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)