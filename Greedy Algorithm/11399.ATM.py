n = int(input())
p = list(map(int, input().split()))
time = 0
answer = []

p.sort()

for i in range(n):
    time = p[i] + time
    answer.append(time)
    
print(sum(answer))