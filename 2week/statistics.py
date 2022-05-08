# 2108번
# 산술 평균, 중앙값, 최빈값, 범위 구하기

import sys

N = int(sys.stdin.readline())


nums = [0]*N
for i in range(N):
    nums[i] = (int(sys.stdin.readline()))

# 산술 평균
print(round(sum(nums)/N))

# 중앙값
nums.sort()
print(nums[N//2+1])

# 최빈값
dic = {}
for i in nums:
    dic[i] = nums.count(i)

max_count = max(dic.values())

if max_count == 1 or max_count == len(nums):
    print('없다.')
for value, count in dic.items():
    if count == max_count:
        print(value)

# 범위 출력
print(nums[-1]-nums[0])


