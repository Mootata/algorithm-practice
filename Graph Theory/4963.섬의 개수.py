from collections import deque

dx, dy = [-1, 1, 0, 0, -1, 1, -1, 1], [0, 0, -1, 1, -1, -1, 1, 1] # 상 하 좌 우 대각선 왼위 왼쪽 아래 오른쪽 위 오른쪽 아래

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    global count
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and field[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
    count += 1

while True:
    w, h = map(int, input().split()) # 지도의 너비 w, 높이 h
    if w == 0 and h == 0:
        break
    field = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    count = 0
    
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and field[i][j] == 1:
                bfs(i, j)
    print(count)