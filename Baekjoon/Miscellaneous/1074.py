import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
ans = 0

while N > 1:
    curr = (2 ** N) // 2
    if r < curr and c < curr:
        N -= 1
        continue
    elif r < curr and c >= curr:
        ans += 4 ** (N - 1)
        c -= curr
    elif r >= curr and c < curr:
        ans += 2 * (4 ** (N - 1))
        r -= curr
    elif r >= curr and c >= curr:
        ans += 3 * (4 ** (N - 1))
        r -= curr
        c -= curr

if r == 0 and c == 0:
    print(ans)
elif r == 0 and c == 1:
    print(ans + 1)
elif r == 1 and c == 0:
    print(ans + 2)
elif r == 1 and c == 1:
    print(ans + 3)
