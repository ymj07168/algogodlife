# 수의 개수 N (1~500,000 / 홀수)
# N개의 줄에 정수들이 주어짐. 각 정수들의 절댓값은 4000을 넘지 x
# 산술평균, 중앙값, 최빈값, 범위 구하기

import math
import sys
from collections import Counter

N = int(sys.stdin.readline())
num_list = []
sum=0
for i in range(N):
    num_list.append(int(sys.stdin.readline()))
    sum += num_list[i]
    
# 산술평균
arithmetic = round(sum / N)

# 중앙값
sorted_list = sorted(num_list) # list.sort()는 값을 반환하지 않는다. 단순실행 / 그에 반해 sorted(리스트)는 리스트를 반환해준다
mid = sorted_list[math.floor(N/2)]

# 최빈값 
# counter 함수 사용시 {가장 많이 등장한 값 : 횟수}의 dic으로 return
count = Counter(sorted_list)
if N <=1 :
    common = count.most_common()
    freq = common[0][0]
else:
    common = count.most_common(2)
    if common[0][1] == common [1][1]:
        freq = common[1][0]
    else:
        freq = common[0][0]

# 범위
min = sorted_list[0] 
max = sorted_list[len(sorted_list)-1]
num_range = max - min

print("{}\n{}\n{}\n{}".format(arithmetic, mid, freq, num_range))