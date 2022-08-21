import sys
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
ans = 0
for _ in range(P):
    x, y = map(int, input().split())
    if X <= x <= X + W and Y <= y <= Y + H:
        ans += 1
        continue
    elif ((X - x) ** 2 + (Y + H // 2 - y) ** 2) ** 0.5 <= H // 2:
        ans += 1
        continue
    elif ((X + W - x) ** 2 + (Y + H // 2 - y) ** 2) ** 0.5 <= H // 2:
        ans += 1
        continue

print(ans)
