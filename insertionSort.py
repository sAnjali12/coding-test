def sort(arr):
    length = len(arr)
    index=1
    while index<length:
        tamp = arr[index]
        chack = index-1
        while(chack>=0 and arr[chack]>tamp):
            arr[chack+1] = arr[chack]
            chack = chack-1
        arr[chack+1] = tamp
        index = index+1
    return arr

arr = [23,0,98,56,3,-56,23456]
insertionSort = sort(arr) 
print (insertionSort)
