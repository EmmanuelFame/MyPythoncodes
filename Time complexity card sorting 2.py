#sort array from max to min

def selection_sort(alist):
    for i in range(0, len(alist) - 1): #outer for 0-8.
        smallest = i
        #print("smallest")
        #print("after assignment")
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
 

cards=[8,3,4,5,6,7,2,9,10]
print(cards)
cards[2],cards[3]=cards[3],cards[2]
print (cards)


selection_sort(cards)
#Ass: Change first and last element
#write in notepad

