import sys
N = int(sys.stdin.readline().rstrip())

words=[]
for _ in range(N):
    words.append(sys.stdin.readline().strip())

# 중복 제거해주기, 길이 순으로 정렬, 사전 순으로 정렬
words_set = set(words)
words = list(words_set)  # 중복 제거된 리스트로
words.sort()
words.sort(key=len)  # key=len :길이순으로 정렬하기

for i in words:
    print(i)