import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
    line1_1 = x2 - x1
    line1_2 = y2 - y1
    line1_3 = (x1 * y2) - (x2 * y1)
    line2_1 = x4 - x3
    line2_2 = y4 - y3
    line2_3 = (x3 * y4) - (x4 * y3)

    det = line1_1 * line2_2 - line2_1 * line1_2

    if det:
        x = (line1_1 * line2_3 - line1_3 * line2_1) / det
        y = (line1_2 * line2_3 - line1_3 * line2_2) / det
        print(f'POINT {x:.2f} {y:.2f}')
    else:
        check = line1_2 * (x3 - x1) - line1_1 * (y3 - y1)
        if check:
            print("NONE")
        else:
            print("LINE")
