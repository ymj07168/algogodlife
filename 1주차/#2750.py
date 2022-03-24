#1
n = int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))

nums.sort()  # 내장함수
nums = nums.sorted()  # 정렬된 리스트 반환
for i in range(n):
    print(nums[i])

#2 선택정렬: n^2
n = int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))

# 오름차순으로 정렬
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if nums[min_index] > nums[j]:  # 가장 작은 수의 인덱스 찾기
            min_index = j
    nums[min_index], nums[i] = nums[i], nums[min_index]  # 위치 바꾸기(최소값을 앞으로 보내준다)

for i in nums:
    print(i)