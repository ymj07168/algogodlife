W = []
K = []

firstOfW, firstOfK, secondOfW, secondOfK, thirdOfW, thirdOfK = 0

for i in range(0, 10):
    W.append(int(input()))
    
for i in range(0, 10):
    K.append(int(input()))
    
for i in range(0, 10):
    if W[i] > firstOfW:
        firstOfW = W[i]
    elif W[i] == firstOfW:
        secondOfW = W[i]
    elif W[i] < firstOfW and W[i] > secondOfW:
        secondOfW = W[i]
    elif W[i] < secondOfW and W[i] > thirdOfW:
        thirdOfW = W[i]

for i in range(0, 10):
    if K[i] > firstOfK:
        firstOfK = K[i]
    elif K[i] == firstOfK:
        secondOfK = K[i]
    elif K[i] < firstOfK and K[i] > secondOfK:
        secondOfK = K[i]
    elif K[i] < secondOfK and K[i] > thirdOfK:
        thirdOfK = K[i]
        
print(firstOfW+secondOfW+thirdOfW, firstOfK+secondOfK+thirdOfK)