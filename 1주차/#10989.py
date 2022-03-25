# 계수 정렬(수의 범위가 작다)
# for문 안에서 append를 사용하게 되면 메모리를 효율적으로 사용하지 X (문제에서 갯수 많음)
import sys
n = int(sys.stdin.readline())

result = [0] * 10001  # 빈 리스트 만들어두기

for _ in range(n):
    result[int(sys.stdin.readline())] += 1
# print(result)

for i in range(10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)