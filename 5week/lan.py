# 백준 1654번
# 랜선 자르기
# https://coblin.xyz/38 참고

import sys

K, N = map(int, sys.stdin.readline().split())

lan = [int(sys.stdin.readline()) for _ in range(K)]

min = min(lan)
max = max(lan)

while min <= max:
    mid = (min + max) // 2

    cnt = 0 # 랜선 수를 카운팅 하는 변수
    for i in lan:
        cnt += i // mid # 랜선을 자른 수

    if cnt >= N: # 랜선을 자른 수가 N보다 클 경우
        min = mid + 1
    else:
        max = mid - 1

print(max)
