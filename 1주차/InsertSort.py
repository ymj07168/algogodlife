# 백준 2750번
print('N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램')
print('(단, 입력되는 수는 절댓값이 1,000보다 작거나 같아야 하며, 중복되지 않는다.)')
while True:
    n = int(input('N 입력(단, N은 1에서 1,000 사이의 자연수이다.): '))
    if 1 <= n <= 1000:
        break
array = []
for _ in range(n):
    num = int(input('N개의 정수 차례로 입력: '))
    if -1000 <= num <= 1000:
        array.append(num)
    else:
        break

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
