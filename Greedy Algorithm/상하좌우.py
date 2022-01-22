n = int(input()) # 공간의 크기
plans = input().split()
x, y = 1, 1
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0] # 동 서 남 북
move_types = ['R', 'L', 'D', 'U']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny

print(x, y)


# N = int(input())
# command = input().split()
# x, y = 1, 1
# for c in command :
#     if c == 'L' and y > 1 : y -= 1
#     elif c == 'R' and y < N : y += 1
#     elif c == 'U' and x > 1 : x -= 1
#     elif c == 'D' and x < N : x += 1

# print(x, y)