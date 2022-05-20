# 백준 2110번
# 공유기 설치

import sys

N, C = map(int, sys.stdin.readline().split())

house = [int(sys.stdin.readline()) for _ in range(N)]

house.sort()

start = 1   # 가장 작은 집 사이 거리
end = house[-1] - house[0]  # 가장 큰 집 사이 거리

result = 0

while start <= end:
    mid = (start + end) // 2

    router = house[0]   # 제일 앞 집에 라우터 설치
    cnt = 1  # 설치 라우터 개수

    for i in house:
        if i >= router + mid:   # mid 거리보다 먼 다음 집에 라우터 설치
            cnt += 1
            router = i

    if cnt >= C:    # 총 라우터 개수 > 설치해야 할 라우터 개수 => 더 넓게 설치
        start = mid + 1
        result = mid
    else:           # 총 라우터 개수 < 설치해야 할 라우터 개수 => 더 좁게 설치
        end = mid - 1

print(result)