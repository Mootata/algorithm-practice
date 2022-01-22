n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0

b2 = sorted(b, reverse = True)
a.sort()

for i in range(n):
    answer += a[i] * b2[i]

print(answer)