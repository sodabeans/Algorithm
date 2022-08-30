import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())

for _ in range(q):
    a, l, r = map(str, input().split())
    ans = 0
    for idx in range(int(l), int(r) + 1):
        if S[idx] == a:
            ans += 1
    print(ans)
