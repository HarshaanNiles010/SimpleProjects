# Bubble sort in python

def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(n-i-1):
			if(arr[j] > arr[j+1]):
				arr[j],arr[j+1] = arr[j+1],arr[j]
	return arr

arr = [9,8,7,6,5,4,3,2,1]
print(f"The original array is {arr}")
print(f"The sorted array is {bubbleSort(arr)}")