def quicksort(array, start, end):
	if start>=end:
		return
	i=start
	j=end
	pivot=array[start]
	while i!=j:
		while array[j]> pivot and i<j:
			j-=1
		while array[i]<=pivot and i<j:
			i+=1
		array[i], array[j]=array[j], array[i]
	array[start]=array[i]
	array[i]=pivot
	quicksort(array, start, i-1)
	quicksort(array, i+1, end)


arr=[33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
quicksort(arr, 0, len(arr)-1)
print(arr)
