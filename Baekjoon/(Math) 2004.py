import sys
input = sys.stdin.readline


def cnt_two_or_five(num, div):
    cnt = 0
    while num > 0:
        num = num // div
        cnt += num
    return cnt


n, m = map(int, input().split())
cnt_2 = cnt_two_or_five(n, 2) - cnt_two_or_five(m, 2) - cnt_two_or_five(n - m, 2)
cnt_5 = cnt_two_or_five(n, 5) - cnt_two_or_five(m, 5) - cnt_two_or_five(n - m, 5)

print(min(cnt_2, cnt_5))
