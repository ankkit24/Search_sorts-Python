#binary search - only for a sorted array
# can convert an array to a sorted one and then search in it
#time complexity is O(log n) which is less than O(n)

def binsearch(arr,l,r,x):
	
	if(r>=l):
		mid = int((l+r)/2)
		
		if (arr[mid]==x):
			return mid
		elif (arr[mid]>x):
			return binsearch(arr,l,mid-1,x)
		else:
			return binsearch(arr,mid+1,r,x)
	else:
		return -1

#test input		
print('Enter array elements:')
arr = map(int, input().split())
x = input('Enter search element')
sort_arr = list(arr)
sort_arr.sort()
print('Sorted array:')
print(sort_arr)

#call the function
result = binsearch(sort_arr,0,len(sort_arr)-1,int(x))	
if result == -1:
	print('Search element not found!!')
else:
	print('Element found at position ',result)
