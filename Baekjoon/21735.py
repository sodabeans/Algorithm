import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [0] + list(map(int, input().split()))  # starting position is 0


def dfs(idx, snowball, time):
    global ans

    if time > M:
        return
    else:
        ans = max(snowball, ans)

    if idx < N - 1:
        dfs(idx + 1, snowball + a[idx + 1], time + 1)
    if idx < N - 2:
        dfs(idx + 2, snowball // 2 + a[idx + 2], time + 1)


ans = 0
dfs(0, 1, 0)
print(ans)
