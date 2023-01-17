import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))
answer = [0] * N
ans = []

while len(tower) > 1:
    curr = tower.pop()
    flag = True
    for i in range(len(tower) - 1, -1, -1):
        if tower[i] > curr:
            answer[len(tower)] = i + 1
            flag = False
            break
    if flag:
        answer[len(tower)] = 0
print(*answer)
