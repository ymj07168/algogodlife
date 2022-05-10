# 1920번
# 수 찾기

def searchBinary(list, n):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2

        if n == list[mid]:
            return 1
        elif n > list[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0

# 존재 값
N = int(input()) ## 사용하지는 않음
Nums = list(map(int, input().split()))

# 검색 값
M = int(input())
Nums2 = list(map(int, input().split()))

# 존재 값 리스트 정렬
Nums.sort()

# 검색
for i in range(M):
    print(searchBinary(Nums, Nums2[i]))