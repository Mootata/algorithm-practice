from collections import deque

n, k = map(int, input().split()) # n은 수빈의 위치, k는 동생의 위치
visited = [0] * 100001

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            break
        for i in (x - 1, x + 1, x * 2): # 앞 또는 뒤로 걷거나 순간이동 하거나.
            if 0 <= i <= 100001 and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)
        
bfs()