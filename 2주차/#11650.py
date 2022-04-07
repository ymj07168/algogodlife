import sys
n = int(sys.stdin.readline())
pos=[]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())  # map(int, input().split())
    pos.append((a,b))

result = sorted(pos, key=lambda x : (x[0], x[1]))
# 람다를 이용하여 정렬의 우선순위를 알려준다
# x좌표를 기준으로 정렬하되, x좌표가(x[0]) 같다면 y좌표(x[1]) 오름차순으로 정렬

for i in range(n):
    print(result[i][0], result[i][1])