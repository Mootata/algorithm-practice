n = int(input())
time = list(range(0, 60))
count = 1

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
    
print(count)