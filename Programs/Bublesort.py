arr=[25,2,6,7,45,67,23,54,65,33,78,46]
def bubblesort(list):
        
        for i in range(0,len(list) - 1):
                for j in range(0,len(list)-1-i):
                        if list[j] > list[j+1]:
                                list[j],list[j+1]=list[j+1],list[j]
        return list
print("Unsorted list is:",arr)

print("Sorted list is:",bubblesort(arr))
