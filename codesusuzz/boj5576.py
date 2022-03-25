from select import KQ_NOTE_WRITE

univ_w = []
univ_k = []

for x in range(10):
    univ_w.append(int(input()))
    
for y in range(10):
    univ_k.append(int(input()))
    
univ_k.sort()
univ_w.sort()

def top3(univ):
    result = 0
    for i in range(7,10):
        result = result + univ[i]
    return result

print(top3(univ_k), top3(univ_w))

#change