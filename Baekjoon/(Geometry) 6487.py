import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if x1 == x2:  # x = x1 = x2
        x_sol_one = x1
    elif y1 == y2:  # y = y1 = y2
        slope_one = 0
        y_int_one = y1
    else:
        slope_one = (y2 - y1) / (x2 - x1)
        y_int_one = y1 - (slope_one * x1)

    if x3 == x4:  # x = x3 = x4
        x_sol_two = x3
    elif y3 == y4:  # y = y3 = y4
        slope_two = 0
        y_int_two = y3
    else:
        slope_two = (y4 - y3) / (x4 - x3)
        y_int_two = y3 - (slope_two * x3)

    x_sol = -(y_int_one - y_int_two) / (slope_one - slope_two)
    y_sol_one = slope_one * x_sol + y_int_one
    y_sol_two = slope_two * x_sol + y_int_two

    if y_sol_one == y_sol_two:
        print(f"POINT {x_sol} {y_sol_one}")
    else:
        print("LINE")
