
a=float(input())
b=float(input())
c=float(input())

x1=0
x2=0
D=b**2-2*a*c
if D>0:
    x1=(-b+D**0.5)/(2*a)
    x2=(-b-D**0.5)/(2*a)
if D==0:
    x1=(-b/(2*a))
    x2=0
if D<0:
    print('err')
print(x1,x2)
