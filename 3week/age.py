# 10814번
# 나이순 정렬

import sys

N = int(sys.stdin.readline())

member = []
for i in range(N):
    age, name = map(str, (sys.stdin.readline().split()))
    age = int(age)
    member.append([age, name])

member = sorted(member, key=lambda a : a[0])

for i in member:
    print(i[0], i[1])


