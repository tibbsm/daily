# Leetcode 1

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

### Brute force ###

def brute(arr, target):
	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[i] == target - arr[j]:
				return [i, j]
	
	return
arr = [2,7,11,15]
print brute(arr, 9)
print brute(arr, 18)


### Loop ###

def loop(arr, target):

	check = {}

	for i in range(len(arr)):
		if target - arr[i] in check:
			return [check[target-arr[i]] ,i ]
		else:
			check[arr[i]] = i


print loop(arr, 9)
print loop(arr, 18)

