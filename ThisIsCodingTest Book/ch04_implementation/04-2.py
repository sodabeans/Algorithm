import sys
input = sys.stdin.readline

N = int(input())
answer = 0

for i in range(N + 1):
    if i == 3 or i == 13 or i == 23:  # hours
        answer += 60 * 60
    else:
        answer += (15 * 60) + (45 * 15)

print(answer)
