'''
ALGORITHM : 

begin BubbleSort(list)

   for all elements of list
      if list[i] > list[i+1]
         swap(list[i], list[i+1])
      end if
   end for
   
   return list
   
end BubbleSort


PSEUDOCODE :


procedure bubbleSort( list : array of items )

   loop = list.count;
   
   for i = 0 to loop-1 do:
      swapped = false
		
      for j = 0 to loop-1 do:
      
         /* compare the adjacent elements */   
         if list[j] > list[j+1] then
            /* swap them */
            swap( list[j], list[j+1] )		 
            swapped = true
         end if
         
      end for
      
      /*if no number was swapped that means 
      array is sorted now, break the loop.*/
      
      if(not swapped) then
         break
      end if
      
   end for
   
end procedure return list


'''

def bubbleSort(ar):
   n = len(ar)
   # Traverse through all array elements
   for i in range(n):
      # Last i elements are already in correct position
      for j in range(0, n-i-1):
         # Swap if the element found is greater than the next element
         if ar[j] > ar[j+1] :
            ar[j], ar[j+1] = ar[j+1], ar[j]


# Worst and Average Case Time Complexity: O(n*n)
# Best Case Time Complexity: O(n).
# Auxiliary Space: O(1)
