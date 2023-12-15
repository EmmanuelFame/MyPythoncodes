def func2(a=4, b=5):

    def inner_func(x):
        return x*x*x

    T=inner_func(a) + inner_func(b)
    return (T)

g=1
h=2
e=func2()#189 (4^3 + 5^3)
print(e)
e=func2(g)#126 (g=1, b=defined value=5)
print(e)
e=func2(g,h)#9 (1^3+2^3)

print(e)
