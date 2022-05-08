# 18870번
# 좌표 압축

import sys

N = int(sys.stdin.readline())

x_list = []

x_list = list(map(int, sys.stdin.readline().split()))

sort_list = sorted(list(set(x_list)))

dic = {sort_list[i]: i for i in range(len(sort_list))}
for i in x_list:
    print(dic[i], end=' ')

# index 함수의 시간 복잡도는 O(N)으로 시간 초과가 난다고 한다...
"""
for i in x_list:
    print(sort_list.index(i), end=' ')
"""




