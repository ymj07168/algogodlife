#1
n = int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))

nums.sort()  # 내장함수
#nums = sorted(nums)  # 정렬된 리스트 반환
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

#3 버블 정렬
def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

n = int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))
bubble_sort(nums)
for i in nums:
    print(i)