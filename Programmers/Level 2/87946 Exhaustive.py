from itertools import permutations


def solution(k, dungeons):
    all_permutations = list(permutations(dungeons))
    answer = -1
    for dun in all_permutations:
        dun_cnt = 0
        tot_k = k
        for min_req_k, sub_k in dun:
            if min_req_k <= tot_k:
                dun_cnt += 1
                tot_k -= sub_k
            else:
                break
        answer = max(answer, dun_cnt)
    return answer
