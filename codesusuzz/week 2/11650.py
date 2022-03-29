# 2주차 6번 - 좌표 정렬하기 (11650번)
''' x좌표 증가순 우선,
x좌표가 같을 때 y좌표 증가순 '''
# import sys

# N = int(sys.stdin.readline())
# x=[]
# y=[]
# for i in range(N):
#     a,b=sys.stdin.readline().split()
#     a,b = int(a), int(b)
#     x.append(a)
#     y.append(b)

# def sort_arr(list_x, list_y):
#     for i in range(len(list_x)):
#         min_idx = i
#         for k in range(i+1, len(list_x)):
#             if list_x[k] < list_x[min_idx]:
#                 min_idx = k
#             elif list_x[k] == list_x[min_idx]:
#                 if list_y[k] < list_y[min_idx]:
#                     list_y[min_idx], list_y[k] = list_y[k], list_y[min_idx] # 작으면 y값을 서로 바꿔준다
#         list_x[i], list_x[min_idx] = list_x[min_idx], list_x[i]
#         list_y[i], list_y[min_idx] = list_y[min_idx], list_y[i] #비교 끝나면 x,y 인덱스 맞춰서 자리 바꿔줌
        
# sort_arr(x,y)
# for i in range(len(x)):
#     print("{} {}".format(x[i], y[i]))

# ✅ 이렇게 풀었더니 시간초과가 났다 ... 내장함수를 써야하는 듯하다

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))
[print(x[0], x[1]) for x in sorted(arr)]