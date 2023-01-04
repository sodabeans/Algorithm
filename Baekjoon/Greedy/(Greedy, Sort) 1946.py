import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores.sort()
    answer = 1
    curr_max = scores[0][1]
    for i in range(1, N):
        if curr_max > scores[i][1]:
            answer += 1
            curr_max = scores[i][1]
    print(answer)
