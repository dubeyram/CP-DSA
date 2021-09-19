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
import math
import re
import bisect
import operator
from collections import Counter, deque


def ReadStr(): return input()
def ReadIntList(): return list(map(int, input().split()))
def ReadStrList(): return list(map(str, input().split()))
def ReadInt(): return int(input())
def ReadMultipleValues(): return map(int, input().split())
def ReadMultipleValuesStr(): return map(str, input().split())


def Count_anagram(arr, k):
    n = len(arr)
    l, r, ans = 0, 0, 0
    current_max = -math.inf
    while(r < n):
        if r-l+1 < k:
            if arr[r]>current_max:
                current_max = arr[r]
        if r-l+1 == k:
            if arr[r]>current_max:
                current_max = arr[r]


            if 
            l += 1

        r += 1
    return ans


arr = ReadIntList()
k = 3

print(Count_anagram(arr,k))
