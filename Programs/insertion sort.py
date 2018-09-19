def insertionsort(list):
    for index in range(1,len(list)):
        value = list[index]
        i=index - 1
        while i >=0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i = i-1
            else:
                break
a=[3,2,5,6,7,1,9]
insertionsort(a)
print(a)



