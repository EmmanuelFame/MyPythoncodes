#sort array from max-min

def bubble_sort_v2(list1):
    #outer loop for transversing the entire list
    has_swapped = True
    while (has_swapped):
        print ('has_swapped is  ', has_swapped)
        has_swapped = False
        for j in range (len(list1)-1):
            print (' j is',j)
            if(list1[j]>list1[j+1]):
                print('    compare, if true, swap',list1[j],'and',list1[j+1])
                list1[j],list1[j+1]=list1[j+1],list1[j]
                has_swapped = True
    return list1
cards=[6,2,7,0,13]
#cards=[8,3,4,5,6,7,2,9,10]
bubble_sort_v2(cards)
print(cards)
print (len(cards))
