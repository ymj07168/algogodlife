# 내풀이 -> 시간초과..
import sys
def compression(n, nums):
    cnt = 0
    for i in range(len(nums)):
        if n > nums[i]:  # 현재수보다 작으면 카운트(같은 수는 카운트X)
            cnt += 1
    return cnt

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(nums)

for i in range(len(nums)):
    print(compression(nums[i], nums), end=' ')

# 내가 찾아본 정답
# 리스트 안에서의 크기 순서를 출력해주면 된다
# 크기순서 -> 0부터 시작
import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

sort_nums = list(sorted(set(nums)))  # 중복된 숫자를 제거하고, 오름차순 정렬된 리스트를 반환한다

dic = {sort_nums[i]: i for i in range(len(sort_nums))}
# sort_nums리스트에서 sort_nums[i]: i 를 넣어준다
for i in nums:
    print(dic[i], end=' ')