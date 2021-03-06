# Insertion sort in python

def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j] 
        i = j-1 
        while (i > -1) and key < A[i]: 
            A[i+1]=A[i] 
            i=i-1 
        A[i+1] = key
    return A



arr = [9,8,7,6,5,4,3,2,1]
print(f"The original array is {arr}")
print(f"The sorted array is {insertionSort(arr)}")



