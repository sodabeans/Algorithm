def solution(routes):
    answer = 1
    routes.sort(key=lambda item: (item[1], item[0]))
    curr_camera = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] <= curr_camera <= routes[i][1]:
            continue
        else:
            curr_camera = routes[i][1]
            answer += 1
    return answer
