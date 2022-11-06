def solution(places):
    answer = []

    for p in places:
        problem = False
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    if 0 <= i - 1 < 5 and 0 <= j - 1 < 5:
                        if p[i - 1][j - 1] == 'P' and (p[i - 1][j] != 'X' or p[i][j - 1] != 'X'):
                            problem = True
                            break
                        if p[i - 1][j] == 'P' or p[i][j - 1] == 'P':
                            problem = True
                            break
                    if 0 <= i + 1 < 5 and 0 <= j + 1 < 5:
                        if p[i + 1][j + 1] == 'P' and (p[i + 1][j] != 'X' or p[i][j + 1] != 'X'):
                            problem = True
                            break
                        if p[i + 1][j] == 'P' or p[i][j + 1] == 'P':
                            problem = True
                            break
                    if 0 <= i - 1 < 5 and 0 <= j + 1 < 5:
                        if p[i - 1][j + 1] == 'P' and (p[i - 1][j] != 'X' or p[i][j + 1] != 'X'):
                            problem = True
                            break
                    if 0 <= i + 1 < 5 and 0 <= j - 1 < 5:
                        if p[i + 1][j - 1] == 'P' and (p[i + 1][j] != 'X' or p[i][j - 1] != 'X'):
                            problem = True
                            break

                    if 0 <= i + 2 < 5 and p[i + 2][j] == 'P':
                        if p[i + 1][j] != 'X':
                            problem = True
                            break
                    if 0 <= j + 2 < 5 and p[i][j + 2] == 'P':
                        if p[i][j + 1] != 'X':
                            problem = True
                            break
                    if 0 <= i - 2 < 5 and p[i - 2][j] == 'P':
                        if p[i - 1][j] != 'X':
                            problem = True
                            break
                    if 0 <= j - 2 < 5 and p[i][j - 2] == 'P':
                        if p[i][j - 1] != 'X':
                            problem = True
                            break
            if problem:
                break
        if problem:
            answer.append(0)
        else:
            answer.append(1)

    return answer
