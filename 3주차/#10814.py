import sys
N = int(sys.stdin.readline().rstrip())

students= []

for _ in range(N):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    # a, b = sys.stdin.readline().split()
    students.append((int(a), b))

students.sort(key=lambda x: x[0])  # 나이 증가하는 순으로

for i in range(N):
    print(students[i][0], students[i][1])