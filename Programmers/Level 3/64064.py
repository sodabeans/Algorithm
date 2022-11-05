import itertools

def solution(user_id, banned_id):
    answer = 0
    cases = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        for idx in range(len(user_id)):
            if len(banned_id[i]) != len(user_id[idx]):
                continue
            flag = True
            for j in range(len(banned_id[i])):
                if banned_id[i][j] == '*':
                    continue
                if banned_id[i][j] != user_id[idx][j]:
                    flag = False
                    break
            if flag:
                cases[i].append(idx)
    possible = (set(_) for _ in itertools.product(*cases))
    possible = set(tuple(set(_)) for _ in possible if len(set(_)) == len(banned_id))
    return len(possible)
