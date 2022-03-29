N = int(input())

x = []
y = []

for i in range (N):
    a,b = input().split() #0,2,4...가 x좌표, 홀수가 y좌표
    a = int(a)
    b = int(b)
    x.append(a)
    y.append(b)

def sort_arr(list_x, list_y):
    for i in range(len(list_x)):
        min_idx = i
        for k in range(i+1, len(list_x)):
            if list_x[k] < list_x[min_idx]:
                min_idx = k
            elif list_x[k] == list_x[min_idx]:
                if list_y[k] < list_y[min_idx]:
                    list_y[min_idx], list_y[k] = list_y[k], list_y[min_idx] # 작으면 y값을 서로 바꿔준다
        list_x[i], list_x[min_idx] = list_x[min_idx], list_x[i]
        list_y[i], list_y[min_idx] = list_y[min_idx], list_y[i] #비교 끝나면 x,y 인덱스 맞춰서 자리 바꿔줌
        
sort_arr(x,y)
for i in range(len(x)):
    print("{} {}".format(x[i], y[i]))