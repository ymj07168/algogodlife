#2750과 같지만 시간초과에 더 신경써야한다
#1. 병합정렬(merge sort)
import sys
n = int(sys.stdin.readline())
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a

    mid = n // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    return merge(left, right)

def merge(left, right):
    result=[]
    left_id, right_id = 0, 0

    #case1 :left, right
    while len(left) > left_id and len(right) > right_id:
        if left[left_id] > right[right_id]:
            result.append(right[right_id])
            right_id += 1
        else:
            result.append(left[left_id])
            left_id += 1
    #case2 : left
    while len(left) > left_id and len(right) <= right_id:
        result.append(left[left_id])
        left_id += 1
    #case3 : right
    while len(left) <= left_id and len(right) > right_id:
        result.append(right[right_id])
        right_id += 1

    return result

nums=[]
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums = merge_sort(nums)
for i in nums:
    print(i)