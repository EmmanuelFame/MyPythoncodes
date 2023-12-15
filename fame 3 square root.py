import math
A = {'a': 4, 'b': 9, 'c': 16, 'd': 25, 'e': 36, 'f': 49, 'g': 64, 'h': 81,'j': 100}
if not 'f' in A: print ('missing')
for key in sorted(A):
    print(key, '=>', A[key])
i = 1
while i<=20:
        print(i**0.5,'is square root of',i)
        i+=1
else:
        print('loop finish')
    

