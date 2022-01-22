from collections import deque

n, m = map(int, input().split()) # N x M 크기의 미로\
maze = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    
    return maze[n - 1][m - 1]
print(bfs(0, 0))