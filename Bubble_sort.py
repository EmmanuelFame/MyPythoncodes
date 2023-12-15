#sort array from max-min

def bubble_sort(list1):
    for i in range(0, len(list1)-1):
        for j in range (len(list1)-1):
            if(list1[j]>list1[j+1]):
                temp=list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1

cards=[13,2,7,5]
bubble_sort(cards)
print(cards)


#Ass
#cards=[8,3,4,,5,6,7,2,9,10]
#cards[2],cards[3]=cards[3],cards[2]
#print(cards)
#change first and last element
#write in notepad this program
