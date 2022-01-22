from collections import deque

n = int(input()) # 노드의 개수 n

tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parents = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)
    
def bfs():
    queue = deque()
    queue.append(1)
    
    while queue:
        node = queue.popleft()
        if not visited[node]:
            for i in tree[node]:
                if not visited[i]: # 두 번 탐색되는 경우 없애기 위해서 (예를들어 1, 6의 간선이 있다면)
                    queue.append(i)# tree[1]에도 6이 있고, tree[6]에도 1이 있기 떄문에 다음에 방문할 노드가
                    parents[i] = node # 방문한 적이 있는지 확인해야함
            visited[node] = True
            
bfs()
    
print(*parents[2:], sep = '\n')