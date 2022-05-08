# 1181번
# 단어 정렬
# 1. 길이가 짧은 것부터 2. 길이가 같으면 사전 순으로

import sys

# 숫자 입력
N = int(sys.stdin.readline())

# 단어 저장할 배열 선언
words = []
# 입력된 단어 배열 삽입
for i in range(N):
    words.append(sys.stdin.readline().strip('\n'))  ## strip으로 '\n' 제거

# 중복값 제거를 위해 set으로 변환
words_set = set(words)
# 다시 리스트로 변환
words = list(words_set)

words.sort(key=lambda x : (len(x), x))

# 출력
for i in words:
    print(i)





