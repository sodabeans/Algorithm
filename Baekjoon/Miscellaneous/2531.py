import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]

ans = 0

for i in range(N):
    start = i
    end = i + k
    dish = {c}
    for j in range(start, end):
        j %= N
        dish.add(belt[j])
    if ans < len(dish):
        ans = len(dish)

print(ans)
