n, m = map(int, input().split())
ice_mold = []
count = 0

for i in range(n):
    ice_mold.append(list(map(int, input())))
    
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if ice_mold[x][y] == 0:
        ice_mold[x][y] = 1
        dfs(x + 1, y) # 상
        dfs(x - 1, y) # 하
        dfs(x, y - 1) # 좌
        dfs(x, y + 1) # 우
        return True
    return False
        
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
                        
print(count)