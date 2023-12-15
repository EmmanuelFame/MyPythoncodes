'''num1= int(input('type a number: '))
num2= int(input('type a number: '))
num3= int(input('type a number: '))
if num1>num2:
    max=num1
    min=num2
else:
    max=num2
    min=num1
if max<num3:
    max=num3
if min>num3:
    min=num3

average=(max+min)/2
print('the max is', max)
print('the min is', min)
print('the average is', average)'''

'''
_min=0
_max=0
for i in range(20):
    num=int(input('type a number: '))
    if num>_max:
        _max=num
print(_max)'''

_min=1000
for i in range(10):
    num=int(input('type a number: '))
    if num%2==0:
        if _min>num:
            _min=num
print(_min)
