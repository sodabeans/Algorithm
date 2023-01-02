import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)
ans = []


def selection():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(N):
        if (ans and ans[-1] > nums[i]) or nums[i] in ans:
            continue
        ans.append(nums[i])
        selection()
        ans.pop()


selection()
