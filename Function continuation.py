def func1(a=3, b=4):

    def inner_func(x):
        return x*x*x

    C=inner_func(a) + inner_func(b)
    return (C)

c=2
d=3
e=func1()#91 3^3 + 4^3
print(e)
e=func1(c)#72 c=2, b=defined value=4
print(e)
e=func1(c,d)# 2^3+3^3

print(e)
Assignment do a similar code and change the defined letters and
submit into the cloud drive.

