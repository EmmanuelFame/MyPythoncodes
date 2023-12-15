operate=str(input('Input operate:'))

if operate=='+':
    print ('operate sum')
    Val1=int(input('Input Val1'))
    Val2=int(input('Input Val2'))
    sum=Val1+Val2
    print('Result is ', sum)
    elif operate=='*':
        print ('operate product')
        Val1=int(input('Input Val1'))
        Val2=int(input('Input Val2'))
        product=Val1*Val2
        print('Result is ', product)
        elif operate=='/':
            print ('operate division')
            Val1=int(input('Input Val1'))
            Val2=int(input('Input Val2'))
            division=Val1/Val2
            print('Result is ', division)
            else : print ('incorrect')

