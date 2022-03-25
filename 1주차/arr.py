warr = []
karr = []
wscore = 0
kscore = 0

for i in range(10):
    warr.append(int(input()))
for i in range(10):
    karr.append(int(input()))
warr.sort()
karr.sort()
for i in range(3):
    kscore += karr.pop()
for i in range(3):
    wscore += warr.pop()

print(wscore, kscore)
