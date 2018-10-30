
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def findLow(arr):

    arr.append(0)
    size = len(arr)

    for i in range(len(arr)):
        if arr[i] < 0 or arr[i] >= size:
            arr[i] = 0

    print arr

    for i in range(len(arr)):
        arr[arr[i]%size] += size
        print arr

    for i in range(1, len(arr)):
        if arr[i]/size == 0:
            return i

    return size

print findLow([3,4,-1,1])
print findLow([1,2,0])
print findLow([2,2,0])
print findLow([2,2])

    

