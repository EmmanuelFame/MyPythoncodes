import random
number = random.randint(1, 10)
H=[1,2,3,4,5,6,7,8,9,10]
def A(number):
    for x in H:
        if x== number == H[0]:
            print('it is unity')
        elif x== number == H[1]:
            print('it is twinny')
        elif x== number == H[2]:
            print('it is triangular')
        elif x== number == H[3]:
            print('it is like a perfect square')
        elif x== number == H[4]:
            print('it is the pentagon agent')
        elif x== number == H[5]:
            print('it is the pentagon agent')
        elif x== number == H[6]:
            print('it is the days in a week')
        elif x== number == H[7]:
            print('it is octa')
        elif x== number == H[8]:
            print('it is new and neuf')
        elif x== number == H[9]:
            print('it is the ultimate number')
            break

print('press A if you need hint and P to pass  ')
hint=str(input())
if hint == 'A':
    A(number)
elif hint == 'P':
    pass
else:
    print('type A in capital if you need Hint or P to pass ')
