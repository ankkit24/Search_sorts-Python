#merge sort - time complexity is O(n logn) < O(n**2)

def sort(arr, l, h):
	if(h>l):
		mid = int((l+h)/2)
		
		#divide the left and right halves
		sort(arr,l,mid)
		sort(arr,mid+1,h)
		
		#merge the halves
		merge(arr,l,mid,h)

def merge(arr,l,mid,h):
	# putting halves into temp arrays
	left = arr[:mid]
	right = arr[mid:]
	
	#merging the 2 halves
	i = j = k = 0
	while(i<len(left) and j<len(right)):
		if(left[i]<right[j]):
			arr[k] = left[i]
			i+=1
		else:
			arr[k] = right[j]
			j+=1
		k+=1
		
	#left over parts added to arr
	while(i<len(left)):
		arr[k] = left[i]
		i+=1
		k+=1
	
	while(j<len(right)):
		arr[k] = right[j]
		j+=1
		k+=1
	
if __name__ == '__main__':
	arr= [12,11,13,5,6,7]
	print('Original array')
	print(arr)
	sort(arr,0,len(arr)-1)
	print('sorted array')
	print(arr)