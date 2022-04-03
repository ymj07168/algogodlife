# 내밑에 몇명이나 있는지
# set으로 중복 제거된 집합을 만들고
# 값:인덱스 형태로 dictionary 정의

# 1. 딕셔너리이름 = {"key값" : "value값"} 
# 2. key 중복 허용 X
# 3. key가 중복 될 경우 마지막에 입력된 key의 value를 출력
# 4. dict[키값] = value 반환


import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num_sorted = sorted(set(num))
dic = {num_sorted[i]:i for i in range(len(num_sorted))}
[print(dic[x], end=' ') for x in num]