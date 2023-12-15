
def linearsearch(lys, element):
    print('lenght of lys is', len(lys))
    for i in range (len(lys)):
        print('compare lys[',i,']', lys[i], 'to element', element)
        if lys[i] == element:
            return i
    return -1


array=[5,8,7,-6,8,0]
print(linearsearch(array, 8))
