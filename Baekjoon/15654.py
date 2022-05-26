import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []


def dfs():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(N):
        if nums[i] not in ans:
            ans.append(nums[i])
            dfs()
            ans.pop()


dfs()
