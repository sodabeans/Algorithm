import sys
input = sys.stdin.readline


def search_paper(square, x, y, end, zero, one):
    target = square[x][y]
    for i in range(x, x + end):
        for j in range(y, y + end):
            if target != square[i][j]:
                zero, one = search_paper(square, x, y, end // 2, zero, one)
                zero, one = search_paper(square, x + end // 2, y, end // 2, zero, one)
                zero, one = search_paper(square, x, y + end // 2, end // 2, zero, one)
                zero, one = search_paper(square, x + end // 2, y + end // 2, end // 2, zero, one)
                return zero, one
    if target == 0:
        zero += 1
    else:
        one += 1
    return zero, one


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]


zero_cnt, one_cnt = search_paper(paper, 0, 0, N, 0, 0)
print(zero_cnt)
print(one_cnt)
