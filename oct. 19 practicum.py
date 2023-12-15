'''#task 1: comparing the sides of a triangle
a=int(input('type the side of the triangle: '))
b=int(input('type the side of the triangle: '))
c=int(input('type the side of the triangle: '))
if a==b and b==c:
    print('equalateral triangle')
elif a==b or b==c:
    print('Isosceles triangle')
else: #a!=b and b!=c:
    print('Scalene triangle')'''

#task 2: user input 3 numbers, find max and min numbers, and calculate the average
#of these min and max
num1= int(input('type a number: '))
num2= int(input('type a number: '))
num3= int(input('type a number: '))
if num1>num2:
    max=num1
else:
    max=num2
if max<num3:
    max=num3
if num1<num2:
    min=num1
else:
    min=num2
if min>num3:
    min=num3

average=(max+min)/2
print('the max is', max)
print('the min is', min)
print('the average is', average)


'''if a1>b2 and c3<a1:
    print('max is a1', a1)
elif a1<b2 and b2>c3:
    print('max is b2', b2)
elif a1>b2 and c3>a1:
    print('max is c3', c3)'''
