import sys
input = sys.stdin.readline

N = int(input())
marble = list(map(int, input().split()))
ans = 0


def dfs(energy):
    if len(marble) == 2:
        global ans
        if ans < energy:
            ans = energy
        return
    for i in range(1, len(marble) - 1):
        energy += marble[i - 1] * marble[i + 1]
        curr = marble[i]
        marble.pop(i)
        dfs(energy)
        marble.insert(i, curr)
        energy -= marble[i - 1] * marble[i + 1]


dfs(0)
print(ans)
