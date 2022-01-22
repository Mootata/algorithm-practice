from collections import deque
import sys

n, m = map(int, input().split()) # 컴퓨터의 수 n, 신뢰하는 관계(방향이 있는 간선)의 수 m

trust = [[] for _ in range(n + 1)]
answers = [0 for _ in range(n + 1)]

for i in range(m):
    t1, t2 = map(int, sys.stdin.readline().split())
    trust[t2].append(t1) # t1이 t2를 신뢰한다. t2에서 t1으로 이동 가능하다는 의미
    
def bfs(k):
    queue = deque()
    queue.append(k)
    visited = [False] * (n + 1)
    visited[k] = True
    count = 1
    
    while queue:
        computer = queue.popleft()
        for i in trust[computer]:
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = True
    
    return count
    
for i in range(1, n + 1):
    if len(trust) > 0:
        answers[i] = bfs(i)
    
answer = sorted([i for i in range(len(answers)) if answers[i] == max(answers)])
print(*answer)