import sys

n = int(sys.stdin.readline())
pos = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    pos.append([x, y])

result = sorted(pos, key=lambda a : (a[1], a[0]))


for i in result:
    print(' '.join(str(s) for s in i))