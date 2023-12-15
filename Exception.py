
try:
    a=int(input('please enter value: '))
except ValueError:
    print ('Input a number please')
else:
    print ('Correct input, next:')
finally:
    print ('Hello world')
try:
    a=int(input('please enter value 1'))
    b=int(input('please enter value 2'))
    c=a/b
except (ValueError, ZeroDivisionError): 
    print ('input correct value (0 and letters are not allowed) ')

