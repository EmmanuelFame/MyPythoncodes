'''x=int(input("input a number"))
y=int(input("input a number"))
X=1
Y=1
if x>y:
    Y= (x+y)/2
    X= 2*x*y
    print(X)
    print(Y)
elif y>x:
    X= (x+y)/2
    Y= 2*x*y
    print(X)
    print(Y)
else:
    print('incorrect input')'''
a=int(input("input base of triangle: "))
b=int(input("input height of triangle: "))
c=int(input("input length of triangle: "))
if a>0 and b>0 and c>0:
    if a<(b+c) and b<(a+c) and c<(b+a):
        A=(a*b)/a
        print('Area of triangle= ', A)
        
    

