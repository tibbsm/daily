# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def productArray(arr):

	size = len(arr)
	left = [0 for i in range(size)]
	right = [0 for i in range(size)]

	left[0] = 1
	right[size - 1] = 1

	for i in range(1, size):
		left[i] = left[i - 1] * arr[i-1]

	for j in range(size - 2, -1, -1):
		right[j] = right[j + 1] * arr[j + 1]

	for k in range(0, size):
		arr[k] = left[k] * right[k] 

#	print left, right
#	print arr
	return arr

arr = [1, 2, 3, 4, 5]

print (arr)
print (productArray(arr))
