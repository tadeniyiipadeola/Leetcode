

def mergesort(list):
    #divide the list by 2 to get the middle index
    mid = len(list)//2
    print(list[mid])
    # partition the list into left and right 
    L = list[:mid]
    R = list[mid:]
    print(L)
    print(R)
    #recursion left
    mergesort(L)
    #recursion right
    mergesort(R)

    return 




array = [34,23,64,32,2,3,64,3,6,6,85,2,4,1,6,7,23,78,56,36,29]
mergesort(array)