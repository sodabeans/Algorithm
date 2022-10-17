def solution(record):
    answer = []
    result = []
    nicknames = dict()
    for r in record:
        curr_record = r.split()
        if curr_record[0] == 'Leave':
            result.append([0, curr_record[1]])
        else:
            if curr_record[0] == 'Enter':
                result.append([1, curr_record[1]])
            nicknames[curr_record[1]] = curr_record[2]
    for entry in result:
        if entry[0] == 0:
            answer.append(f'{nicknames[entry[1]]}님이 나갔습니다.')
        else:
            answer.append(f'{nicknames[entry[1]]}님이 들어왔습니다.')

    return answer
