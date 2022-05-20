# 백준 2805번
# 나무 자르기

import sys
# N은 나무의 수, M은 나무의 길이
N, M = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

min = 1
max = max(tree)

while min <= max:
    mid = (min + max) // 2

    sum_tree = 0
    for i in tree:
        if i > mid:
            sum_tree += i - mid

    if sum_tree >= M: # 랜선을 자른 수가 M보다 클 경우
        min = mid + 1
    else:
        max = mid - 1

print(max)