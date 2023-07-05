import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bowling = list(map(int, input().split()))
answer = 0

for i in range(N):
    curr = bowling[i]
    for j in range(i + 1, N):
        if bowling[j] != curr:
            answer += 1

print(answer)
