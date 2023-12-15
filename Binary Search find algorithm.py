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
        #print('func _quicksort, begin is',begin, 'end is',end)
        if begin >= end:
            #print ('begin',begin, 'is grter thn or eq to end', end)
            return
        #print('we call funtion partition and we give begin,',begin ,'and end', end,)
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

def Binary_search(lys, val):
    first= 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index=mid
        else:
            if val<lys[mid]:
                last=mid-1
            else:
                first= mid+1
    return index

array=[5,8,7,-6,9,0]
print(array)
quick_sort(array)
print(array)
print(Binary_search(array, 8))
input()
