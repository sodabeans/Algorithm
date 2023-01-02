import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
curr = []


def selection(depth):
    if depth == M:
        print(' '.join(map(str, curr)))
        return
    prev = 0
    for i in range(N):
        if prev != nums[i]:
            if curr and curr[-1] > nums[i]:
                continue
            prev = nums[i]
            curr.append(prev)
            selection(depth + 1)
            curr.pop()


selection(0)
