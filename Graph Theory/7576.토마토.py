from collections import deque

m, n = map(int, input().split()) # M x N 크기의 상자 
box = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
answer = 0
queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j)) # 탐색은 익은 토마토들부터 시작해야 하므로 미리 큐에 넣어줌

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0: # 박스를 벗어나지 않고 익지 않은 토마토 일 때 
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))
    
bfs()
for i in box:
    for j in i: # 박스의 모든 토마토를 확인
        if j == 0: # 익지 않은 토마토가 있다면
            print(-1) # -1 출력하고
            exit(0) # 종료
    answer = max(answer, max(i)) # 가장 큰 값이 정답
print(answer - 1) # 익은 토마토가 1이어서 시작이 1이었으므로 1을 빼줘야 걸린 일수가 나옴