Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def selection_sort(alist):
...     for i in range(0, len(alist) - 1): #outer for 0-8.
...         print('i is',i)
...         smallest = i
...         
...         for j in range(i + 1, len(alist)): #inner for 0-8
...             print ('j is',j)
...             if alist[j] < alist[smallest]:
...                 print(alist[j],'<', alist[smallest],' is true')
...                 smallest = j
...         #print('change', alist[i], alist[smallest])
...         alist[i], alist[smallest] = alist[smallest], alist[i]
...         
... cards=[8,3,4,5,2,7,9]
... print(cards)
... selection_sort(cards)
