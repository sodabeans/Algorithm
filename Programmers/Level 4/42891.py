def solution(food_times, k):
    curr = 0
    total = sum(food_times)
    total -= k
    if total <= 0:
        return -1

    while k:
        if food_times[curr] > 0:
            food_times[curr] -= 1
            k -= 1
        curr += 1
        if curr == len(food_times):
            curr = 0

    return curr + 1
