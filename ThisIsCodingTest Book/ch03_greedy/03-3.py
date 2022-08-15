# 숫자 카드 게임
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = 0

for _ in range(N):
    curr_row = list(map(int, input().split()))
    ans = max(ans, min(curr_row))

print(ans)
