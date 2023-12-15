#sort array from max. to min.

def selection_sort(alist):
    for i in range(0, len(alist) - 1): 
        print('i is',i)
        smallest = i
        for j in range(i + 1, len(alist)): 
            print ('j is',j)
            if alist[j] < alist[smallest]:
                print(alist[j],'<', alist[smallest],' is true')
                smallest = j
        print('change', alist[i], alist[smallest])
        alist[i], alist[smallest] = alist[smallest], alist[i]
        
cards=[12,5,13,6,15,0]
#print(len(cards))
print(cards)
selection_sort(cards)
print(cards)

