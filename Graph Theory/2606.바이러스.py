from collections import deque

computers = int(input()) # 컴퓨터의 수
links = int(input()) # 간선의 수
network = [[] for _ in range(computers + 1)]
visited = [False for _ in range(computers + 1)]

for i in range(links):
    c1, c2 = map(int, input().split())
    network[c1].append(c2)
    network[c2].append(c1) 
    
def bfs():
    queue = deque()
    queue.append(1)
    count = 0
    
    while queue:
        v = queue.popleft()
        if not visited[v]:
            visited[v] = True
            count += 1
            for i in network[v]:
                queue.append(i)
                
    return count - 1 # 1번 컴퓨터를 통해서 감염되는 컴퓨터의 수 이기 때문에 1번 컴퓨터는 제외
    
print(bfs())