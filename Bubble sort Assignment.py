#sort array from max-min

def bubble_sort(list1):
    #outer loop for transversing the entire list
    for i in range(0, len(list1)-1):
        print ('i is',i)
        for j in range (len(list1)-1):
            print (' j is',j)
            if(list1[j]>list1[j+1]):
                print('    compare, if true, swap',list1[j],' ',list1[j+1])
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1
cards=[6,2,7,0,13]
#cards=[8,3,4,5,6,7,2,9,10]
bubble_sort(cards)
print(cards)
print (len(cards))
