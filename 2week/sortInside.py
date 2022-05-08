# 1472번
# 소트인사이드

import sys

N = list(sys.stdin.readline())

# 맨 마지막 원소 '/n' 삭제
del N[-1]
# 문자 원소 정수로 변환
list_a = list(map(int, N))

list_a.sort(reverse=True)

# join()으로 숫자가 포함된 리스트 문자열로 변환
for i in list_a:
    result = ''.join(str(s) for s in list_a)
print(result)