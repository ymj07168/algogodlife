# 2751번
# 병합 정렬
# 왜 시간 초과 나는지 이유 모르겠음
import sys

def merge_sort(a):
    n = len(a)

    if n <= 1:
        return a

    mid = n // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    i, j, k = 0, 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            result.append(left[i])
        else:
            result.append(right[j])

    result += left[i:]
    result += right[j:]

    return result

num = int(sys.stdin.readline())

before = []
for _ in range(num):
    before.append(int(sys.stdin.readline()))

before = merge_sort(before)
for i in before:
    print(i)

