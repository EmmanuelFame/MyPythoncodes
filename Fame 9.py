Num1=int(input("Enter First Number"))
Num2=int(input("Enter Second Number"))

print ("Which operations would you like to perform")
ch = input("Enter any of this specific operations +,-,*,/,^,**:")

result = 0
if ch == '+':
    result = Num1 + Num2
    print(Num1, ch, Num2, ":", result)
elif ch == '-':
    result = Num1 - Num2
    print(Num1, ch, Num2, ":", result)
elif ch == '*':
    result = Num1 * Num2
    print(Num1, ch, Num2, ":", result)
elif ch == '/':
    result = Num1 - Num2
    print(Num1, ch, Num2, ":", result)
elif ch == '**':
    result = Num1 ** Num2
    print(Num1,ch,Num2,":", result)
else:
    print("imput character is not recognised!")
#print (Num1, ch, Num2, ":", result)
