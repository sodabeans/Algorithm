import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
curr = []
visited = [0] * (N + 1)

ans = list()


def selection(depth):
    if depth == M:
        if curr not in ans:
            ans.append(curr.copy())
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            curr.append(nums[i])
            selection(depth + 1)
            curr.pop()
            visited[i] = 0


selection(0)


for element in ans:
    print(' '.join(map(str, element)))