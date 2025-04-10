from collections import deque


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
R, C, K = map(int, input().split())
grid = [[0] * C for _ in range(R + 2)]
fairies = []


def check_row_number_of_column(col):
    final_row = 1
    for row in range(1, R + 1):
        if grid[row][col] == 0 and grid[row + 1][col] == 0 and grid[row - 1][col] == 0:
            final_row = row
    return final_row - 1


def move_south(r, c, d):
    check_valid_directions = [(2, 0), (1, -1), (1, 1)]  ## 중심 기준
    for dr, dc in check_valid_directions:
        new_r = r + dr
        new_c = c + dc
        if not (0 <= new_r < (R + 2)) or not (0 <= new_c < C) or grid[new_r][new_c] != 0:
            return []
    # 남쪽으로 내려갈 수 있다면
    r += 1
    return [r, c, d]


def rotate_west(r, c, d):
    check_valid_directions = [(-1, -1), (0, -2), (1, -1), (1, -2), (2, -1)]  ## 중심 기준
    for dr, dc in check_valid_directions:
        new_r = r + dr
        new_c = c + dc
        if not (0 <= new_r < (R + 2)) or not (0 <= new_c < C) or grid[new_r][new_c] != 0:
            return []
    # 서쪽으로 회전할 수 있다면
    r += 1
    c -= 1
    d -= 1
    return [r, c, d]


def rotate_east(r, c, d):
    check_valid_directions = [(-1, 1), (0, 2), (1, 1), (1, 2), (2, 1)]  ## 중심 기준
    for dr, dc in check_valid_directions:
        new_r = r + dr
        new_c = c + dc
        if not (0 <= new_r < (R + 2)) or not (0 <= new_c < C) or grid[new_r][new_c] != 0:
            return []
    # 동쪽으로 회전할 수 있다면
    r += 1
    c += 1
    d += 1
    return [r, c, d]


def place_the_cross(center_r, center_c, exit_dir, turn):
    grid[center_r][center_c] = turn
    for dir_idx in range(4):
        dr, dc = directions[dir_idx]
        nr = center_r + dr
        nc = center_c + dc
        if (0 <= nr < (R + 2)) and (0 <= nc < C):
            if dir_idx == exit_dir:
                grid[nr][nc] = (-1) * turn
            else:
                grid[nr][nc] = turn


def BFS(center_r, center_c):
    visited = [[0] * C for _ in range(R + 2)]
    queue = deque()
    queue.append((center_r, center_c))
    visited[center_r][center_c] = 1
    max_row = center_r

    while queue:
        curr_r, curr_c = queue.popleft()
        current_idx = grid[curr_r][curr_c]
        for dr, dc in directions:
            new_r = curr_r + dr
            new_c = curr_c + dc
            if 0 <= new_r < (R + 2) and 0 <= new_c < C and visited[new_r][new_c] == 0:
                if abs(grid[new_r][new_c]) == abs(current_idx):
                    visited[new_r][new_c] = 1
                    queue.append((new_r, new_c))
                    max_row = max(max_row, new_r)
                elif current_idx < 0 and grid[new_r][new_c] != 0:
                    visited[new_r][new_c] = 1
                    queue.append((new_r, new_c))
                    max_row = max(max_row, new_r)
    # for row in visited:
    #     print(row)
    return max_row


def repeat_rotation(r, c, d):
    current_r = r
    current_c = c
    current_d = d
    while True:
        new_coords = move_south(current_r, current_c, current_d)
        if len(new_coords):
            new_r = new_coords[0]
            new_c = new_coords[1]
            new_d = new_coords[2]
            if new_r > current_r:
                current_r = new_r
                current_c = new_c
                current_d = new_d
        else:
            new_coords = rotate_west(current_r, current_c, current_d)
            if len(new_coords):
                new_r = new_coords[0]
                new_c = new_coords[1]
                new_d = new_coords[2]
                if new_r > current_r:
                    current_r = new_r
                    current_c = new_c
                    current_d = new_d
            else:
                new_coords = rotate_east(current_r, current_c, current_d)
                if len(new_coords):
                    new_r = new_coords[0]
                    new_c = new_coords[1]
                    new_d = new_coords[2]
                    if new_r > current_r:
                        current_r = new_r
                        current_c = new_c
                        current_d = new_d
                else:
                    break
    return current_r, current_c, current_d


answer = 0
for current_turn in range(1, K + 1):
    c_i, d_i = map(int, input().split())
    c_i -= 1
    r_i = check_row_number_of_column(c_i)

    final_r, final_c, final_d = repeat_rotation(r_i, c_i, d_i)

    place_the_cross(final_r, final_c, final_d, current_turn)

    if final_r < 2:
        grid = [[0] * C for _ in range(R + 2)]
        continue
    else:
        answer += BFS(final_r, final_c) - 1

print(answer)
