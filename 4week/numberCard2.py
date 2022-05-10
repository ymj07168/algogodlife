# 10816번
# 숫자 카드 2

# 검색 값의 최소 인덱스 찾기
def firstIndex(list, n):
    start = 0
    end = len(list) - 1
    fi = -1 # 못 찾았을 경우

    while start <= end:
        mid = (start + end) // 2

        if n == list[mid]:
            fi = mid
            end = mid - 1   ## 최소 인덱스 찾기 위함
        elif n > list[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return fi

# 검색 값의 마지막 인덱스 찾기
def lastIndex(list, n):
    start = 0
    end = len(list) - 1
    li = -1                 # 못 찾았을 경우 -1

    while start <= end:
        mid = (start + end) // 2

        if n == list[mid]:
            li = mid
            start = mid + 1   # 최대 인덱스 찾기 위함
        elif n > list[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return li

# 상근이가 가지고 있는 숫자 카드 개수
N = int(input())
# 상근이의 숫자 카드에 적혀있는 정수
NCard = list(map(int, input().split()))

# 상근이가 몇 개 가지고 있는지 구해야 할 정수 개수
M = int(input())
# 상근이가 몇 개 가지고 있는지 구해야 할 정수
MCard = list(map(int, input().split()))

NCard.sort()

result = []
for i in MCard:
    if firstIndex(NCard, i) != -1:
        result.append(lastIndex(NCard, i)-firstIndex(NCard, i)+1)
    else:
        result.append(0)

for i in result:
    print(i, end=" ")