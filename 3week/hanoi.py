# 11729번
# 하노이 탑 이동 순서

import sys
N = int(sys.stdin.readline())

# 원반 no개를 x기둥에서 y기둥으로 옮김
def move(no: int, x: int, y: int) -> None:
    if no > 1:
        move(no - 1, x, 6-x-y)

    print(f'{x} {y}')

    if no > 1:
        move(no - 1, 6-x-y, y)

print(2**N - 1)
move(N, 1, 3)

