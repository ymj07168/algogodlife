# 1427 소트인사이드

import sys
import math
n = int(sys.stdin.readline())
temp=n
num=[]


while (temp/10 >= 1):
    num.append(math.floor(temp%10))
    temp=math.floor(temp/10)
if temp/10 < 1:
    num.append(temp)

num.sort()
result=0
while num:
    result += num[len(num)-1] * (10**(len(num)-1))
    num.pop()
    
print(result)