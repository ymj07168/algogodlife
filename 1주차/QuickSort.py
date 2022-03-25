# 백준 2751번
while True:
    n = int(input())
    if 1 <= n <= 1000000:
        break
array = []
for _ in range(n):
    num = int(input())
    if -1000000 <= num <= 1000000:
        array.append(num)
    else:
        break

def quick_sort(array, start, end):
    if start>=end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)