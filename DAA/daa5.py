#O(nlogn)

import random


def partition(array, low, high, piv):
    pivot = array[high]
    i = low - 1
    print(i)
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
	if low < high:
		if randomized:
			piv = random.randrange(low, high)
		else:
			piv = high
		pi = partition(array, low, high, piv)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)


randomized = bool(int(input("Enter 0 for fixed, 1 for randomized pivot : ")))
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)
randomized = True
quickSort(data, 0, size - 1)
print("Sorted Array in Ascending Order:")
print(data)






## Quick Sort

# array = [35, 50, 15, 25, 80, 20, 90, 45]



# def partition(low, high):
#   pivot = array[low]
#   i = low
#   j = high 
  
#   while(i<j):
#     while(array[i]<= pivot):
#       i=i+1
#     while(array[j]>pivot):
#       j=j-1
#     if(i<j):
#       array[i], array[j] = array[j], array[i]

#   array[j], array[low] = array[low], array[j] 
  
#   return j

# def quickSort(low, high):
#   if(low < high):
#     pi = partition(low, high)
    

#     quickSort(low, pi-1)
#     quickSort(pi+1, high)
  

# quickSort(0, len(array) - 1)
# print(array)
