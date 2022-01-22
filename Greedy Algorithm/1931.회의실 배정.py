n = int(input())
time = []
count = 0
last_end = 0 # 최근 회의가 끝나는 시간

for _ in range(n):
    time.append(tuple(map(int, input().split())))
    
time.sort(key = lambda x: (x[1], x[0])) # 회의가 끝나는 시간을 기준으로 정렬하고 끝나는 시간이 같은 회의 끼리는 시작 시간을 기준으로 정렬

for start, end in time: 
    if start >= last_end:
        count += 1
        last_end = end
        
print(count)