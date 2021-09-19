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


def first_negative(N,Array,k):
    l,r =0,0
    negative = []
    ans = []
    while(r<N):
        if r-l+1<k:
            if Array[r]<0:
                negative.append(Array[r])
                
        if r-l+1==k:
            if Array[r]<0:
                negative.append(Array[r])
            if len(negative)>0:
                ans.append(negative[0])
            else:
                ans.append(0)
            if Array[l]<0:
                negative.remove(Array[l])
            l+=1
        r+=1
    return ans

N = ReadInt()
Array = ReadIntList()
k = ReadInt()

ans = first_negative(N,Array,k)
for i in ans:
    print(i,end=" ")