n = int(input())
array = sorted(list(map(int, input().split())))
group = 0
count = 0

for fear in array:
    count += 1
    if count >= fear:
        group += 1
        count = 0

print(group)