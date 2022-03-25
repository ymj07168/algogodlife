# 내 풀이
import sys
W_score = []
K_score = []
for i in range(10):  # 처음 10개가 W, 그다음 10개가 K
    W_score.append(int(sys.stdin.readline()))
for i in range(10):
    K_score.append(int(sys.stdin.readline()))

W_score.sort(reverse=True)
K_score.sort(reverse=True)

a, b = 0, 0  # 고득점자 3명의 점수 합산
for i in range(3):
    a += W_score[i]
    b += K_score[i]
print(a, b)