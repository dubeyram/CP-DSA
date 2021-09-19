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


def Count_anagram(text, pattern, k):
    pattern_count = dict(Counter(pattern))
    count = len(pattern_count)
    n = len(text)
    l, r, ans = 0, 0, 0

    while(r < n):
        if r-l+1 < k:
            if text[r] in pattern_count:
                pattern_count[text[r]] -= 1
                if pattern_count[text[r]] == 0:
                    count -= 1

        if r-l+1 == k:
            if text[r] in pattern_count:
                pattern_count[text[r]] -= 1
                if pattern_count[text[r]] == 0:
                    count -= 1
            if count == 0:
                ans += 1

            if text[l] in pattern_count:
                if pattern_count[text[l]] ==0:
                    count+=1
                pattern_count[text[l]] += 1
            l += 1

        r += 1
    return ans


text = "aabaabaa"
pattern = "aaba"
k = len(pattern)

print(Count_anagram(text, pattern, k))
