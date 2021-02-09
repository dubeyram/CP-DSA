class Solution:
    # Merge sort TC: O(NlogN)
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1: # Important
            mid = len(nums)//2 # Finding the mid of array
            L = nums[:mid] # Dividing the array elements into 2 halves
            R = nums[mid:] 

            self.sortArray(L) # Sorting the first half
            self.sortArray(R) # Sorting the second half

            # Merging
            i = j = k = 0
            while i < len(L) and j < len(R):
                #...
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = R[j]
                    j += 1
                    k += 1

            # Checking if any element was left
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
        # Edge case [0] Just return nums
        return nums
    
