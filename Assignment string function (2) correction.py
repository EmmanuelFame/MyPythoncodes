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
print(concatenation(S1,S2))
print(Doubling(S1,4))
print(Functionmylen(S1))
print(Accessatindex(S2,4))
print(Extractioncut(S2,1,3))
print(Extractioncutwithstep(S2,1,6,2))





