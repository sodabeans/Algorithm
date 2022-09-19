import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())

    # NONE special cases
    if x1 == x2 and y1 != y2 and x3 == x4 and y3 != y4:  # two vertical lines
        print("NONE")
        continue
    if x1 != x2 and y1 == y2 and x3 != x4 and y3 == y4 :  # two horizontal lines
        print("NONE")
        continue

    # LINE special cases
    if x1 == x2 == x3 == x4 or y1 == y2 == y3 == y4:
        print("LINE")
        continue

    # POINT special cases
    if x1 == x2 and y1 != y2:  # only first line is vertical
        slope = (y4 - y3) / (x4 - x3)
        y_int = y3 - (slope * x3)
        ans_y = slope * x1 + y_int
        print(f'POINT {x1:.2f} {ans_y:.2f}')
        continue
    if x3 == x4 and y3 != y4:  # only second line is vertical
        slope = (y2 - y1) / (x2 - x1)
        y_int = y1 - (slope * x1)
        ans_y = slope * x3 + y_int
        print(f'POINT {x3:.2f} {ans_y:.2f}')
        continue

    slope_one = (y2 - y1) / (x2 - x1)
    y_int_one = y1 - (slope_one * x1)
    slope_two = (y4 - y3) / (x4 - x3)
    y_int_two = y3 - (slope_two * x3)

    if slope_one == slope_two:
        if y_int_one == y_int_two:
            print("LINE")
        else:
            print("NONE")
    else:
        ans_x = (y_int_one - y_int_two) / (slope_two - slope_one)
        ans_y = (slope_two * y_int_one - slope_one * y_int_two) / (slope_two - slope_one)
        print(f'POINT {ans_x:.2f} {ans_y:.2f}')
