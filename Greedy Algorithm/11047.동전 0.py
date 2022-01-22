n, k = map(int, input().split()) # 동전의 종류 n, 가치의 합 k
value = []
count = 0

for i in range(n):
    value.append(int(input()))
    
for i in value[::-1]:
    if k >= i:
        count += k // i
        k = k % i
print(count)