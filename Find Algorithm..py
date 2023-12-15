
def linearsearch(lys, element):
    print('lenght of lys is', len(lys))
    for i in range (len(lys)):
        print('compare lys[',i,']', lys[i], 'to element', element)
        if lys[i] == element:
            return i
    return -1


array=[5,7,8,-6,8,0]
print(linearsearch(array, 8))
#Ass used print and take two case, when I find and don't find,
#and also write on paper how the program works.

def partition(array, begin, end):
    #print('func partition, begin is',begin, 'end is',end)
    pivot=begin
    #print(' part_pivot',pivot ,'is eq to begin',begin)
    #print(' loop from', begin+1,' to ',end+1)
    for i in range(begin+1, end+1):
        if array [i] <= array [begin]:
            #print('  ',array[i] , ' is ls thn or eq to begin', array[begin])
            pivot+=1
            #print('   pivot is ',pivot)
            #print('  ',array[i], ' is swapped with', array[pivot])
            array[i], array[pivot]=array[pivot], array [i]
    #print('loop end ',array[pivot], ' is swapped with', array[begin])
    array[pivot], array[begin]= array[begin], array [pivot]
    #print(array)
    return pivot


def quick_sort(array, begin=0, end=None):
    #print('func quick_sort, begin is =',begin, 'end is =',end)
    if end is None:
        end= len(array) - 1
        #print('end is none, end is ', end)
    def _quicksort(array, begin, end):
        if begin>= end:
            return
        pivot=partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)
    
#array=[5,1,8,2,1,6]
#print(quick_sort(array))
#quick_sort(array)
#print(array)
