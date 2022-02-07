def solution(id_list, report, k):
    answer = []
    tmp = []
    reported_id = {i: [] for i in id_list}
    
    for r in set(report):
        r = r.split()
        reported_id[r[1]].append(r[0])
    
    for ed in reported_id:
        if len(reported_id[ed]) >= k:
            tmp += reported_id[ed]
    
    for i in id_list:
        answer.append(tmp.count(i))
    
    return answer
