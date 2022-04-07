n = input()

result = []
for i in n:
    result.append(int(i))
result.sort(reverse=True)

for i in result:
    print(i, end='')