def func1(a, b):

    def inner_func(x):
        return x*x*x

    return inner_func(a) - inner_func(b)
c=5
d=3
e=func1(c,d)
print (e)
