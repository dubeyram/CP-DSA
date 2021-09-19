 # '''
# ⠀   ⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀
# ⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀  ⡏⠀⠀⠀⠀⠀⢷
# ⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇
# ⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⣸⠀श्रीराम⠀⡇
# ⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀  ⡇
# ⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀ ⡼
# ⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞⠀
# ⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀
# ⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
# ⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
# ⣿⣿⣿⣿⣿⣿⣿⣧⣀⣿………⣀⣰⣏⣘⣆⣀⠀
# # '''
# C:\Users\DELL\AppData\Local\Programs\Python\Python37
import math, re, bisect, operator
from collections import Counter, deque

ReadStr = lambda: input()
ReadIntList = lambda: list(map(int, input().split()))
ReadStrList = lambda: list(map(str, input().split()))
ReadInt = lambda: int(input())
ReadMultipleValues = lambda: map(int, input().split())
ReadMultipleValuesStr = lambda: map(str, input().split())

def Max_sum_subarray(N,Array,k):
    l= 0;r= l+k
    current_sum = 0
    maximum_sum = -math.inf
    while(r<=N):
        current_sum = sum(Array[l:r])
        if current_sum >maximum_sum:
            maximum_sum = current_sum
        l+=1
        r+=1
    return (maximum_sum)

N = ReadInt()
Array = ReadIntList()
k =ReadInt()
print(Max_sum_subarray(N,Array,k))



