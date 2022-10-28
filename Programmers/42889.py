def solution(N, stages):
    score_cnt = {x: 0 for x in range(1, N + 1)}
    stages.sort()
    total_people = len(stages)
    for idx in range(len(stages)):
        if stages[idx] > N:
            break
        score_cnt[stages[idx]] += 1
        if idx == len(stages) - 1:
            score_cnt[stages[idx]] /= total_people
            break
        if stages[idx] != stages[idx + 1]:
            tmp = score_cnt[stages[idx]]
            score_cnt[stages[idx]] /= total_people
            total_people -= tmp
    
    return list(dict(sorted(score_cnt.items(), key=lambda x: (-x[1], x[0]))).keys())

  """
# (timeout) 70.4
def solution(N, stages):
    answer = []
    cnt_list = [0 for _ in range(N)]
    for idx in range(len(stages)):
        if stages[idx] > N:
            continue
        cnt_list[stages[idx] - 1] += 1
    
    user_cnt = len(stages)
    for idx in range(N):
        tmp = cnt_list[idx]
        cnt_list[idx] /= user_cnt
        user_cnt -= tmp
    
    cnt_list = [(cnt_list[idx], idx + 1) for idx in range(N)]
    cnt_list.sort(key=lambda x:(-x[0], x[1]))
    
    return [x[1] for x in cnt_list]
"""
