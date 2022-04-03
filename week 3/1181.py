# 소문자 단어 N개 입력받음
# 길이순 > 알파벳순
import sys

N = int(sys.stdin.readline().strip())
dictionary = []
for i in range(N):
    word = sys.stdin.readline().strip()
    if word not in dictionary:
        dictionary.append(word)
dictionary.sort()
dictionary.sort(key=lambda x:len(x))
for i in range(len(dictionary)):
    print(dictionary[i])