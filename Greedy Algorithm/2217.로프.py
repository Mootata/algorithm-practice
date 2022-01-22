n = int(input()) # 로프의 개수
ropes = []
answer = 0

for i in range(n):
    ropes.append(int(input()))

ropes.sort(reverse = True)

for i in range(0, n): # 1 ~ n
    ropes[i] = ropes[i] * (i + 1)

print(max(ropes))

# k개의 로프로 중량이 w인 물체를 들어올릴 때, 각 로프에는 w/k의 중량이 걸림
# 오름차순으로 정렬 했을 때 가장 작은 값의 k배의 무게를 들 수 있음