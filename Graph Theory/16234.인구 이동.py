from collections import deque

n, l, r = map(int, input().split()) # N x N 크기의 땅, 인구차이 L명 이상, R명 이하
nations = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
days = 0

def bfs(x, y):
    queue = deque()
    union = deque()
    queue.append((x, y))
    union.append((x, y))
    visited[x][y] = True
    population = nations[x][y]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(nations[x][y] - nations[nx][ny]) <= r:
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    visited[nx][ny] = True
                    population += nations[nx][ny]
                    
    for i, j in union:
        nations[i][j] = population // len(union)
        
    return len(union)
                    
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    is_move = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    is_move = True
                    
    if not is_move:
        break
    days += 1
    
print(days)

# 먼저 bfs로 한바퀴 돌아서 열린 국경을 그래프로 만들고 그 그래프를 다시 bfs함수로 돌면서 체크하는게 맞는듯 ?