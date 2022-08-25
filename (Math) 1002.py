import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
            continue
        else:
            print(0)
            continue
    else:
        a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if r1 + r2 < a or abs(r1 - r2) > a:
            print(0)
            continue
        elif r1 + r2 == a:
            print(1)
            continue
        else:
            print(2)
            continue
