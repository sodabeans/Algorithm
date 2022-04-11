import sys
input = sys.stdin.readline

R, C = map(int, input().split())
puzzle = [input().rstrip() for _ in range(R)]

ans = list()

for i in range(R):
    tmp = ''
    for j in range(C):
        if puzzle[i][j] != '#':
            tmp += puzzle[i][j]
        if puzzle[i][j] == '#' or j == C - 1:
            if len(tmp) > 1:
                ans.append(tmp)
            tmp = ''

for j in range(C):
    tmp = ''
    for i in range(R):
        if puzzle[i][j] != '#':
            tmp += puzzle[i][j]
        if puzzle[i][j] == '#' or i == R - 1:
            if len(tmp) > 1:
                ans.append(tmp)
            tmp = ''

ans.sort()
print(ans[0])
