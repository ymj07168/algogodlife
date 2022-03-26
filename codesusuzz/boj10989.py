# 카운팅 정렬
'''
최댓값이 정해져 있을 때,
정렬할 값이 양수일때 사용

값들을 서로 비교하지 않고도 정렬할 수 있다는게 포인트

시간복잡도 O(n)
'''

# 방법 1. counting sort
# 방법 2. 10001개짜리 리스트를 만들어 0으로 초기화하고 입력값이 들어올때마다 인덱스에 +1해주기

import sys

def third_sort():
    n = int(sys.stdin.readline())
    list = [0] * 10001
    for i in range(n):
        idx_num = int(sys.stdin.readline())
        list[idx_num] += 1
    
    for i in range(10001):
        if list[i] != 0:
            for k in range(list[i]):
                print(i)
        
# 카운팅소트로 했는데 자꾸 시간초과 났음.. 

def counting_sort(arr):
    # arr : 입력받을 배열
    # C : 요소별 횟수 저장한 다음 누적합 담을 배열
    # B : 출력 배열, 처음에는 비어 있음, A 요소값의 역순으로 채워짐
    C = [0] * (10001)
    B = [0] * len(arr)
    
    for i in range(len(arr)):
        C[arr[i]] += 1 # arr의 요소별 갯수를 C에 저장
        
    for i in range(1, len(C)):
        C[i] += C[i-1] # C에 각 요소 누적합을 저장
        
    # 이제 arr 요소들의 역순으로 B에 저장해나감
    # 즉 C에 저장된 누적합의 번호가 arr의 역순 요소가 B의 몇번 자리를 차지하는지를 나타냄
    
    arr.reverse()
    for i in range(len(arr)):
        B[C[arr[i]] - 1] = arr[i]
        C[arr[i]] -= 1
        
    return B