n = int(input())
pos = []
for _ in range(n):
    a, b = map(int, input().split())
    pos.append([a, b])

pos.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(pos[i][0], pos[i][1])
