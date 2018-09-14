# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Same as leet 01_twosum.py

def findtwo(arr, k):
	
	check = {}

	for i in range(len(arr)):
		
		if arr[i] in check:
			return True
		else:
			check[k - arr[i]] = True 		
		
	return False
	
print findtwo([10, 15, 3, 7], 17)
print findtwo([11, 15, 3, 7], 17)
