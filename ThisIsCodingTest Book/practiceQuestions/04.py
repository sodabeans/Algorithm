import sys
input = sys.stdin.readline

N = int(input())
coins = list(map(int, input().split()))
coins.sort()
answer = 1

for i in range(N):
    if coins[i] > answer:
        break
    answer += coins[i]

print(answer)
