import sys
input = sys.stdin.readline

N = int(input())
plan = list(map(str, input().rstrip().split(' ')))
x, y = 1, 1

for p in plan:
    if p == 'R' and y < N:
        y += 1
    elif p == 'L' and y > 1:
        y -= 1
    elif p == 'D' and x < N:
        x += 1
    elif p == 'U' and x > 1:
        x -= 1

print(x, y)
