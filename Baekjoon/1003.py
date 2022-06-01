import sys
input = sys.stdin.readline

cnt_zero = [0 for _ in range(41)]
cnt_one = [0 for _ in range(41)]
cnt_zero[0] = 1
cnt_one[1] = 1

for i in range(2, 41):
    cnt_zero[i] = cnt_zero[i - 1] + cnt_zero[i - 2]
    cnt_one[i] = cnt_one[i - 1] + cnt_one[i - 2]

T = int(input())

for _ in range(T):
    N = int(input())
    print(f'{cnt_zero[N]} {cnt_one[N]}')
