# '''

# ⠀   ⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀
# ⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀  ⡏⠀⠀⠀⠀⠀⢷
# ⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇
# ⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀श्रीराम⠀⡇
# ⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀  ⡇
# ⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀ ⡼
# ⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞⠀
# ⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀
# ⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
# ⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
# ⣿⣿⣿⣿⣿⣿⣿⣧⣀⣿………⣀⣰⣏⣘⣆⣀⠀
# # '''
import math
from collections import Counter
ReadStr = lambda : input()
ReadList = lambda : list(map(int,input().split()))
ReadInt = lambda : int(input())
ReadMultipleValues = lambda :map(int,input().split())


# Sum of Array Without using any loop
def Sum_Of_list(arr, n, i):
    sum=0;i+=1
    if i==n:
        return 0
    sum += arr[i] + Sum_Of_list(arr,n,i)

    return sum

n = ReadInt()
arr = ReadList()
i=-1
print(Sum_Of_list(arr,n,i))
    



# count of n length binary string without two consecutive one
def String_recursion(n):
    if n==1:
        return 2
    elif n==2:
        return 3
    return String_recursion(n-1) + String_recursion(n-2)


n = ReadInt()
print(String_recursion(n))





def N_natural_numbers_recursive(n):
    if n==1:
        print(1)
        return 
    print(n)
    N_natural_numbers_recursive(n-1)
    # print("Yes")
    print(n)
    
(N_natural_numbers_recursive(5))



def Fibonacci_recursive(n):
    if n==1:
        return 0
    elif n==2 :
        return 1
    
    return Fibonacci_recursive(n-1)+Fibonacci_recursive(n-2)
print(Fibonacci_recursive(14))

a,b =0,1
n =6
for i in range(1,15):
    a,b = a+b, a
print(b)






def Factorial_recursion(n):
    if n==1:
        return 1
    return n* Factorial_recursion(n-1)
n = ReadInt()
print(Factorial_recursion(n))