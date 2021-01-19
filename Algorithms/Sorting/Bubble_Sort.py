# # Python3 Optimized implementation 
# # of Bubble sort 

# # An optimized version of Bubble Sort 
# def bubbleSort(arr): 
# 	n = len(arr) 

# 	# Traverse through all array elements 
# 	for i in range(n): 
# 		swapped = False

# 		# Last i elements are already 
# 		# in place 
# 		for j in range(0, n-i-1): 

# 			# traverse the array from 0 to 
# 			# n-i-1. Swap if the element 
# 			# found is greater than the 
# 			# next element 
# 			if arr[j] > arr[j+1] : 
# 				arr[j], arr[j+1] = arr[j+1], arr[j] 
# 				swapped = True

# 		# IF no two elements were swapped 
# 		# by inner loop, then break 
# 		if swapped == False: 
# 			break
		
# # Driver code to test above 
# arr = [64, 34, 25, 12, 22, 11, 90] 

# bubbleSort(arr) 

# print ("Sorted array :") 
# for i in range(len(arr)): 
# 	print ("%d" %arr[i],end=" ") 

n = int(input())
s = input()
count=0
if "00" not in s and "11" not in s:
    print(0)

else:
    s = list(s)

    for i in range(1,n):
        if s[0]==s[1]!=s[2]:
            s[0]=s[2]
            count +=1
        elif s[i]==s[i-1]=="1":
            s[i]="0"
            print("yes")
            count+=1
        elif s[i]==s[i-1]=="0":
            s[i]="1"
            count+=1
        print(s)
    print(count)