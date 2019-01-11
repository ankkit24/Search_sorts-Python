# bubble sort - nested for loops - (O(n**2))
# ** swapped = False - to optimize the algo

def bsort(arr):
	for i in range(len(arr)):
		swapped = False
		for j in range(len(arr)-1-i):
			if(arr[j]>arr[j+1]):
				arr[j],arr[j+1] = arr[j+1],arr[j]
				swapped = True
		if(swapped == False):
			break

if __name__ == '__main__':
	arr = [2,5,3,4,9,5,7]
	print('Original array:',arr)
	bsort(arr)
	print('Bubble sorted array:',arr)