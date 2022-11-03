import math

def solution(fees, records):
    answer = []
    cars = {}
    total_fee = {}

    for r in records:
        time, curr_car, inout = r.split()
        hour, minute = time.split(':')
        hour = int(hour)
        minute = int(minute)
        if inout == 'IN':
            cars[curr_car] = (hour, minute)
            if curr_car not in total_fee:
                total_fee[curr_car] = 0
        else:
            start_hr, start_min = cars[curr_car]
            if minute - start_min < 0:
                total_time = (minute - start_min + 60) + (hour - start_hr - 1) * 60
            else:
                total_time = (minute - start_min) + (hour - start_hr) * 60

            total_fee[curr_car] += total_time
            cars.pop(curr_car)

    for car in cars:
        start_hr, start_min = cars[car]
        if 59 - start_min < 0:
            total_time = (59 - start_min + 60) + (car - start_hr - 1) * 60
        else:
            total_time = (59 - start_min) + (23 - start_hr) * 60
        total_fee[car] += total_time
    total_fee = sorted(total_fee.items())

    for _, curr_time in total_fee:
        curr_ans = fees[1]
        if curr_time >= fees[0]:
            curr_time -= fees[0]
            curr_ans += math.ceil(curr_time / fees[2]) * fees[3]
        answer.append(curr_ans)

    return answer
