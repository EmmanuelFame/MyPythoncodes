def quick_sort(sequence):
    lenght = len(sequence)
    if lenght <= 1:
        return sequence
    else:
       #print('operate pop before', sequence)
        pivot = sequence.pop()
       #print(pivot)
       #print('operate pop after', sequence)

    items_greater = []
    #print('items', items_greater)
    items_lower = []

    for item in sequence:
        #print('item in loop', item)
        if item > pivot:
            #print('items_greater before appending', items_greater)
            items_greater.append(item)
            #print('items_greater after appending', items_greater)
        else:
            #print('items_lower before appending', items_lower)
            items_lower.append(item)
           # print('items_lower after appending', items_lower)
    print(' lower, pivot ,greater', items_lower,pivot,items_greater)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
print(quick_sort([5,8,7,-6,9,0]))

'''#original version
def quick_sort(sequence):
    length = len(sequence)
    if length #less than= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item #greater than pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)'''



