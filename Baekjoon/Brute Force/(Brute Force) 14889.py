from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
ans = 50 * N
teams = list(combinations([i for i in range(N)], N // 2))

for idx in range(len(teams) // 2):
    team_1 = 0
    team_2 = 0
    for i in teams[idx]:
        for j in teams[idx]:
            team_1 += S[i][j]
    for i in teams[len(teams) - idx - 1]:
        for j in teams[len(teams) - idx - 1]:
            team_2 += S[i][j]
    ans = min(ans, abs(team_1 - team_2))

print(ans)
