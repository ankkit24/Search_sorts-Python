# heap_sort - uses the concept of complete binary tree
# tc- O(n logn) -> heapify ->O(log n)

def heapify(arr, n, i):
	largest = i 
	l = 2 * i + 1
	r = 2 * i + 2
	
	if(l<n and arr[l]>arr[largest]):
		largest = l
	if(r<n and arr[r]>arr[largest]):
		largest = r
	if(largest != i):
		arr[i],arr[largest] = arr[largest],arr[i]
		heapify(arr, n, largest)

def heapsort(arr):
	n = len(arr)
	# Going bottom up build a max heap
	for i in range(n, -1, -1): # nth to 0th element, going upwardss
		heapify(arr, n, i)
		
	# swap the root with the last element and then heapify root
	for i in range(n-1, 0, -1): # from the last element to root+1
		#swap root with ith element
		arr[i],arr[0] = arr[0],arr[i]
		heapify(arr,i,0) 
		
if __name__ == '__main__':
	arr = [2,5,3,5,6,8,6,9,4]
	print('Original array:',arr)
	heapsort(arr)
	print('Heap sorted array:',arr)