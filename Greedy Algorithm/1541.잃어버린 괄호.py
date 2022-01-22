formula = input().split('-')
answer = 0

for i in formula[0].split('+'): # 첫번째 값은 무조건 더해줌
    answer += int(i)
    
for i in formula[1:]: # 두번쨰 값부터 각 값을 더해서 빼줌
    for j in i.split('+'):
        answer -= int(j)

print(answer)

# 10-20+30-10+40 같은 경우에는 10, 20+30, 10+40으로 나누어지고
# 코드 4번째 줄에서 10을 answer에 더해줌 그 다음 20+30을 연산해서 answer에 빼주고, 10+40도 마찬가지
# 이는 괄호를 하나만 치는 것이 아니라 적절하게 여러개 칠 수 있기 때문에 -를 기준으로 나누어 담은
# 값들을 모두 더해서 뺴주면 되기 때문임