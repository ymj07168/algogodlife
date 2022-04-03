N = int(input())
members = []
for i in range(N):
    age, name = map(str,input().split())
    age = int(age)
    members.append((age,name))
members.sort(key=lambda x:x[0])
[print(x[0], x[1]) for x in members]

# int, str 형변환 안해줘서 에러났다 ㅠ