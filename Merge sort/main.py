

def mergesort(list):
    if len(list) > 1:
        #divide the list by 2 to get the middle index
        mid = len(list)//2
        print("middle index is: ",list[mid])
        # partition the list into left and right 
        L = list[:mid]
        R = list[mid:]
        print("Left lists are: ", L)
        print("Right lists are: ", R)
        #recursion left
        mergesort(L)
        #recursion right
        mergesort(R)
        
        i=j=k=0

        while i<len(L) and j <len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k+=1

        #checking if any element was left
        while i < len(L):
            list[k] = L[i]
            i+=1
            k+=1

        while j< len(R):
            list[k] = R[j]
            j+=1
            k+=1

        return 

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


array = [34,23,64,32,2,3,64,3,6,6,85,2,4,1,6,7,23,78,56,36,29]
mergesort(array)
printList(array)