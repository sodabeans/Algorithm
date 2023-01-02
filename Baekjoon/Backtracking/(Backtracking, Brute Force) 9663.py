import sys
input = sys.stdin.readline

N = int(input())
ans = 0
positions = [0 for _ in range(N)]


def check(curr):
    for idx in range(curr):
        if positions[curr] == positions[idx] or abs(positions[curr] - positions[idx]) == curr - idx:
            return False
    return True


def count_queens(curr):
    global ans
    if curr == N:
        ans += 1
    else:
        for i in range(N):
            positions[curr] = i
            if check(curr):
                count_queens(curr + 1)


count_queens(0)
print(ans)
