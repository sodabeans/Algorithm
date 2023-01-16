import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))
answer = [0] * N
idx = N - 1
curr_tower = N - 1
prev = tower.pop()

while tower:
    curr = tower.pop()
    if prev < curr:
        for i in range(idx, N):
            if answer[i] != 0:
                break
            answer[i] = idx
        prev = curr
        idx -= 1
    else:
        idx -= 1
        prev = max(prev, curr)

print(answer)
