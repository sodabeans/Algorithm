import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]


def count_paper(a, b, length):
    if length == 1:
        ans[paper[a][b]] += 1
        return
    curr = paper[a][b]
    flag = True
    for i in range(a, a + length):
        for j in range(b, b + length):
            if curr != paper[i][j]:
                flag = False
                break
            if not flag:
                break
    if not flag:
        new_length = length // 3
        for i in range(3):
            for j in range(3):
                count_paper(a + i * new_length, b + j * new_length, new_length)
    else:
        ans[paper[a][b]] += 1
        return


count_paper(0, 0, N)
print(ans[-1])
print(ans[0])
print(ans[1])
