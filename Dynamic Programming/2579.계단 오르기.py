n = int(input()) # ęłë¨ě ě n
points = [0] + [int(input()) for _ in range(n)] + [0]

dp = [0, points[1], points[1] + points[2]]

for i in range(3, n + 1):
    dp.append(max(dp[i - 2], dp[i - 3] + points[i - 1]) + points[i])
    
print(dp[-1])