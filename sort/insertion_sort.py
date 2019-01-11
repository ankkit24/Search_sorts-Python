#time complexity O(n^2)

def insertion_sort(li):
	for i in range(1,len(li)):
		x = li[i]
		j = i-1
		while(j>=0) and (li[j]>x):
			li[j+1]=li[j]
			j-=1
		li[j+1]=x
	return li
	
if __name__ == "__main__":
	arr = [2,5,4,3,2,1,6]
	print('Original Array: ', arr)
	arr = insertion_sort(arr)
	print('Sorted array: ',arr)
	