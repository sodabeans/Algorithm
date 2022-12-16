import sys
input = sys.stdin.readline

N = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]
answer = 0

while N:
    A, B = map(int, input().split())
    for i in range(A, A + 10):
        for j in range(B, B + 10):
            if not paper[i][j]:
                paper[i][j] = 1
                answer += 1
    N -= 1

print(answer)
