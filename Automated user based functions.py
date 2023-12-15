def concatenation(S1,S2):
    return S1+S2
def Doubling(s,count):
    return s*count
def Functionmylen(S1):
    return len(S1)
def Accessatindex(S2,num):
    return (S2[num])
def Extractioncut(S2,num1,num2):
    return (S2[num1:num2])
def Extractioncutwithstep(S2,num1,num2,num3):
    return(S2[num1:num2:num3])

S1 = 'Applied '
S2 = 'Programming'
UserChoice = ""
while UserChoice != "exit":
    UserChoice =input('Enter what you want to do with the program, c/d/l/a/e/ex ')
    if UserChoice == 'c':
        print(concatenation(S1,S2))
    elif UserChoice == 'd':
        print(Doubling(S1,4))
    elif UserChoice == 'l':
        print(Functionmylen(S1))
    elif UserChoice == 'a':
        print(Accessatindex(S2,4))
    elif UserChoice == 'e':
        print(Extractioncut(S2,1,3))
    elif UserChoice == 'ex':
        print(Extractioncutwithstep(S2,1,6,2))
    else: print ('incorrect operate')










