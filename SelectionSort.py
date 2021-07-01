# Selection Sort in python

def selectionSort(arr):
	n = len(arr)
	for i in range(n-1):
		mini = i
		for j in range(i+1,n):
			if(arr[j] < mini):
				mini = j
		arr[i],arr[mini] = arr[mini],arr[i]
	return arr

arr = [9,8,7,6,5,4,3,2,1]
print(f"the original array is {arr}")
print(f"the sorted array is {selectionSort(arr)}")