import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())
cnt = [[0] * 26 for _ in range(len(S))]

cnt[0][ord(S[0]) - 97] = 1
for idx in range(1, len(S)):
    cnt[idx][ord(S[idx]) - 97] = 1
    for j in range(26):
        cnt[idx][j] += cnt[idx - 1][j]

for _ in range(q):
    input_arr = input().split()
    if int(input_arr[1]) > 0:
        ans = cnt[int(input_arr[2])][ord(input_arr[0]) - 97] - cnt[int(input_arr[1]) - 1][ord(input_arr[0]) - 97]
    else:
        ans = cnt[int(input_arr[2])][ord(input_arr[0]) - 97]
    print(ans)
