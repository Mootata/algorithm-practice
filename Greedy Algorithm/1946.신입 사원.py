import sys

t = int(input())

for i in range(t):
    scores = []
    count = 1
    last = 0
    
    for j in range(int(input())):
        scores.append(tuple(map(int,sys.stdin.readline().split())))
    scores.sort()
    
    for i in range(1, len(scores)):
        if scores[i][1] < scores[last][1]:
            count += 1
            last = i
        if scores[last][1] == 1:
            break
    
    print(count)
