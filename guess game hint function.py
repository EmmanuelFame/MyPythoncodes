import random
number = random.randint(1, 10)
B= guess = int(input("Guess a number between 1 and 10: ",))

def cont():
        if guess != number:
                print('Wrong, press H if you need a hint:  ')
                return 
def win():
    if guess == number:
        print('congratulations my champion, you got it!!!')
    return B
def hintland():
            i=1
            while i<=10:
                if number==1:
                    A=print('it"s unity')
                    break
                elif number==2:
                    A=print('it"s twinny')
                    break
                elif number==3:
                    A=print('it"s triangular')
                    break
                elif number==4:
                    A=print('it"s like a perfect square')
                    break
                elif number==5:
                    A=print('it"s the pentagon agent')
                    break
                elif number==6:
                    A=print('it"s inverted 9')
                    break
                elif number==7:
                    A=print('it"s the days in a week')
                    break
                elif number==8:
                    A=print('it"s octa')
                    break
                elif number==9:
                    A=print('it is neuf in french')
                    break
                elif number==10:
                    A=print('it"s the ultimate number')
                    break
                elif A != int():
                    print('wrong! guess only between 1-10')
                    break
                elif hint==('P'): 
                    pass    
                else:
                    print('type A or P')
                return 

def ask_4_help():
        H=input('type H for help or P for pass: ')
        #while H != H:
         #       break
        #if H == H: hintland()

win()
cont()
ask_4_help()
        
#print(number)
    
    




