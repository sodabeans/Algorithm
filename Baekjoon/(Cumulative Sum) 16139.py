import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())
cnt = [[0 for _ in range(len(S))] for _ in range(26)]

for idx in range(len(S)):
    cnt[ord(S[idx]) - 97][idx] += 1

for _ in range(q):
    a, l, r = map(str, input().split())
    print(sum(cnt[ord(a) - 97][int(l):int(r)+1]))
