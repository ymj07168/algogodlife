'''
✅ 문제
N개의 수가 주어졌을 때,
이를 오름차순으로 정렬하라.

✅ 입력
첫째 줄에 수의 개수 N (1000 이하) 이 주어진다.
둘째 줄부터 N개의 줄에 수가 주어진다.
이 수는 절댓값이 1000보다 작거나 같은 정수이다.
수는 중복되지 않는다.

✅ 출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를
한 줄에 하나씩 출력한다.
'''

'''
📌 선택 정렬
sol 1. 새로운 리스트를 만들고,
인덱스 0번부터 차례로 뽑아서 나머지 요소들과 비교해
새 리스트에 순서대로 추가하는 방법.
계산 복잡도 O(n^2)

sol 2. 원래 리스트에서 하나씩 뽑아서,
더 작은 수가 나오면 순서를 바꾸는 방법.
계산 복잡도 O(n^2)
'''


def sort_select_1():
    N = int(input())
    arr = []
    for i in range(N):
        k = int(input())
        arr.append(k)
    
    while arr:
        min_idx = 0
        for i in range(len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        min_num = arr.pop(min_idx)
        print(min_num)
        
def sort_select_2():
    # 첫 인덱스값 뽑아서 그 뒤 수와 비교, 
    N = int(input())
    arr = []
    for i in range(N):
        k = int(input())
        arr.append(k)
        
    for i in range(len(arr)):
        min_idx = i
        for x in range(i+1, len(arr)):
            if arr[x] < arr[min_idx]:
                '''
                temp = arr[min_idx]
                arr[min_idx] = arr[x]
                arr[x] = temp 로 짰는데
                if문에서 굳이 바꿀 필요 없음
                for문 다 돌고 나가서 바꿔도 괜찮다
                '''
                min_idx = x
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # for문 끝나고 한꺼번에 교환
        print(arr[i])
        
sort_select_2()