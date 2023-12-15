'''#user input 10 numbers in [-10,30], find the quantity of odd numbers
a=0
b=0
for i in range(10):
    u=int(input('type a number: '))
    if -10<=u<=30:
        a+=1
        print('valid number! ')
        if u%2!=0 and u<0:
            b+=1
            print('odd input ')
    else:
        print('invalid number! ')
print('total valid inputs = ',a,'total odd inputs in range[-10,30]= ',b)
#user input 10 numbers in [-20,20], find the sum of even numbers <0 & >5
a=0
b=0
c=0
for i in range(10):
    u=int(input('type a number: '))
    if -20<=u<=20:
        a+=1
        print('valid number! ')
        if (u<0 or u>5) and u%2==0:
            b+=u
            print('sum of u in range u>5 and u<0',b)
            c+=1
    else:
        print('invalid number! ')
print('total valid inputs = ',a,'total even numbers in range 0<u<5= ',c)
print('total sum of numbers in range (u<0 or u>5)= ',b)
'''
a=20%15
print(a)
