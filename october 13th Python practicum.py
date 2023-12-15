#task1 - finding the quantity of even numbers using the cycle ##FOR##
'''count=0
for i in range(1,6):
    num=int(input('input your numbers to check: '))
    if num % 2 == 0:
        count+=1
        print('HUrray it is even')
    else:
        print('OOps it is odd')
print('total no. of even numbers is(are):', count)'''




#task2 - finding the quantity of even numbers using the cycle ##WHILE##
'''i=1
count=0
while (i<=5):
    i+=1
    num=int(input('input your numbers to check: '))
    if num % 2 == 0:
        count+=1
        print('HUrray it is even')
    else:
        print('OOps it is odd')
print('total no. of even numbers is(are):', count)
'''
'''
#task3 - finding the number that's greater than 5 using the ##WHILE##

i=1
count=0
j=int(input('input the total numbers you want to consider: '))
while (i<=j):
    i+=1
    num=int(input('input the sequence of numbers you want to consider: '))
    if num > 5:
        count+=1
        print('This number is greater than 5:', num , '> 5')
    else:
        print('Nopes, try again!', num, '<= 5')
print('this is the total number of numbers greater than 5: ', count)



#task4 - finding the number that's greater than 5 using the ##FOR##
count=0        
j=int(input('input the total numbers you want to consider: '))
for i in range(j):
    num=int(input('input the sequence of numbers you want to consider: '))
    if num > 5:
        count+=1
        print('This number is greater than 5:', num , '> 5')
    else:
        print('Nopes, try again!', num, '<= 5')
print('this is the total number of numbers greater than 5: ', count)

count= 0
num=int(input('input your number:'))
while num!=0:
    if num < 9 and num % 2!= 0:
        count+=1
    num=int(input('input your number:'))
print('the quantity of odd number less than 9 is', count)

x = 5
i=1
for i in range(100):
    i+=1
    print (i,'*',x, '=', i*x)'''

count = 0
i=0
num=int(input('input your number:'))
while num!=0 and i<5:
        if 2<num<8:
            count+=1
            print(num)


