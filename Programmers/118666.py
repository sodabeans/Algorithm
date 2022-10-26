def solution(survey, choices):
    answer = ''
    score_cnt = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    type_list = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    for idx in range(len(survey)):
        if choices[idx] > 4:
            score_cnt[survey[idx][1]] += choices[idx] - 4
        elif choices[idx] < 4:
            score_cnt[survey[idx][0]] += 4 - choices[idx]
    
    for idx in range(4):
        if score_cnt[type_list[idx][0]] >= score_cnt[type_list[idx][1]]:
            answer += type_list[idx][0]
        else:
            answer += type_list[idx][1]
            
    return answer
    
