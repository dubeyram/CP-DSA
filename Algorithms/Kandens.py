#Longest Sum Subarray....Using Kandens algo with 0(n) complexity.

from sys import maxsize 

def maxsumSubarray(arr , arr_size):

    # Intialize varibale
    current_sum = 0
    max_sum = -maxsize-1 

    # Loop over all the element of array
    for i in range(0 , arr_size):


        current_sum = current_sum +arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum<0:
            current_sum = 0
            
    return (max_sum)

# Time Complexity: O(n)
# Algorithmic Paradigm: Dynamic Programming

# Take input from user length of array and array Element
arr_size = int(input("Enter the size: "))
arr = list(map(int ,input().split()))

# Calling the maxsumSubarray function
print(maxsumSubarray(arr , arr_size))

