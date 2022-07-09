import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
curr = []
visited = [0] * (N + 1)


def selection(depth):
    if depth == M:
        print(' '.join(map(str, curr)))
        return
    prev = 0
    for i in range(N):
        if not visited[i] and prev != nums[i]:
            visited[i] = 1
            prev = nums[i]
            curr.append(prev)
            selection(depth + 1)
            curr.pop()
            visited[i] = 0


selection(0)
