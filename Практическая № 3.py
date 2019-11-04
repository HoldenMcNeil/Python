a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if c<a and c<b:
    print('min',c)
elif a<b and a<c:
    print("min",a)
elif b<c and b<a:
    print("min",b)
if c>a and c>b:
    print("max",c)
elif a>b and a>c:
    print("max",a)
elif b>c and b>a:
    print("max",b)
