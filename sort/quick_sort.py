# quick sort - time complexity -> O(n^2)
# uses the divide and conquer strategy

def qsort(arr, l, h):
	if(l<h):
		pivot = partition(arr,l,h)
		
		qsort(arr,l,pivot-1)
		qsort(arr,pivot+1,h)

def partition(arr,l,h):
	i = l-1
	pivot = arr[h] # can take anything as the pivot
	
	for j in range(l,h+1):
		if(arr[j]<=pivot):
			i+=1
			arr[i],arr[j] = arr[j],arr[i]
	return i

if __name__ == '__main__':
	arr = [10,8,5,7,16,2]
	print('Original array:',arr)
	print('Sorted array:',qsort(arr,0,len(arr)-1))
	