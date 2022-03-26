# 병합 정렬
'''
리스트의 길이가 0 또는 1이면 이미 정렬된 것으로 본다. 
그렇지 않은 경우에는 정렬되지 않은 리스트를 절반으로 잘라 
비슷한 크기의 두 부분 리스트로 나눈다.
각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.
https://i.stack.imgur.com/YlHqG.gif
'''
N = int(input())
list = []
for i in range(N):
    list.append(int(input()))

def merge_sort(arr):
    N = len(arr)
    if N <= 1:
        return
    mid = N // 2
    g1 = arr[:mid]
    g2 = arr[mid:]
    
    merge_sort(g1)
    merge_sort(g2)
    
    arr_idx = 0
    idx_1 = 0
    idx_2 = 0
    
    while idx_1 < len(g1) and idx_2 < len(g2):
        if g1[idx_1] < g2[idx_2]:
            arr[arr_idx] = g1[idx_1]
            idx_1 += 1 # g1의 첫째만 인정받았으니 .. g2는 여전히 첫째가 남아있음
            arr_idx += 1
        else:
            arr[arr_idx] = g2[idx_2]
            idx_2 += 1
            arr_idx += 1
        
    # 둘 중 하나가 끝났을 때
    while idx_1 < len(g1):
        arr[arr_idx] =  g1[idx_1]
        idx_1 += 1
        arr_idx += 1

    while idx_2 < len(g2):
        arr[arr_idx] =  g2[idx_2]
        idx_2 += 1
        arr_idx += 1

merge_sort(list)
for i in range(len(list)):
    print(list[i])