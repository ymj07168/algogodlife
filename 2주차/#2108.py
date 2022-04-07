import sys
from collections import Counter
n = int(sys.stdin.readline())
nums=[]
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

def ave(nums):
    result = sum(nums)  # 합계
    return round(result / n)  # 반올림 함수 사용.

def middle(nums):
    nums.sort()
    return nums[len(nums) // 2]

def freq(nums):
    # Counter를 이용해 빈도수를 구해주고, most_common(2)를 사용하여 빈도수가 높은 숫자 2개를 가져온다
    cnt = Counter(nums).most_common(2)
    if len(nums) > 1 and cnt[0][1] == cnt[1][1]:  # 최빈값이 여러개인 경우(두개가 같음)
        return (cnt[1][0])
    else:
        return (cnt[0][0])

def diff(nums):
    nums.sort()  # 오름차순 정렬
    return nums[len(nums)-1] - nums[0]

print(ave(nums))
print(middle(nums))
print(freq(nums))
print(diff(nums))