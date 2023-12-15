def quick_sort(sequence):
    lenght= len(sequence)
    if len(sequence)<=1:
        return sequence

    else:
        pivot=sequence.pop

    items_greater=[]
    items_lower=[]

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
print(quick_sort([2,3,5,9,1,0,12]))

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

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

