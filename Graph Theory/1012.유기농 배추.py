from collections import deque

t = int(input()) # 테스트 케이스
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    field[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append((nx, ny))
        
for i in range(t):
    m, n, k = map(int, input().split()) # M x N 크기의 배추 밭에 심어진 배추의 수 k
    field = [[0 for _ in range(n)] for _ in range(m)]
    count = 0
    
    for j in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
        
    for x in range(m):
        for y in range(n):
            if field[x][y] == 1:
                bfs(x, y)
                count += 1
            
    print(count)