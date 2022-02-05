t = int(input()) # 테스트 케이스 수 t

for i in range(t):
    n = int(input())
    count = [[1, 0], [0, 1]]
    for i in range(2, n + 1):
        count[0].append(count[0][i - 1] + count[0][i - 2])
        count[1].append(count[1][i - 1] + count[1][i - 2])
    print(count[0][n], count[1][n], end=' ')
    
# 0과 1이 호출되는 수도 피보나치 수와 동일한 방식으로 증가함