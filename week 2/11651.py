# 11651번. 좌표정렬 2

import sys

N = int(input())
arr = []
for i in range(N):
    a,b = map(int, input().split())
    arr.append((b,a))
    
[print(x[1], x[0]) for x in sorted(arr)]