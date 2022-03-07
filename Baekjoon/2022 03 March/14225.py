from itertools import combinations

N = int(input())
S = list(map(int, input().split()))
combi = []

for i in range(1, N+1):
    for x in list(combinations(S, i)):
        combi.append(sum(x))
combi = list(set(combi))
combi.sort()

i = 0
answer = 1

while i < len(combi):
    if combi[i] == answer:
        answer += 1
        i += 1
    else:
        break

print(answer)