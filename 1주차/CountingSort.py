# 백준 10989번
while True:
    n = int(input())
    if 1 <= n <= 1000000:
        break
array = []
for _ in range(n):
    num = int(input())
    if 1 <= num <= 10000:
        array.append(num)
    else:
        break

count = [0] * (max(array) + 1)
for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
