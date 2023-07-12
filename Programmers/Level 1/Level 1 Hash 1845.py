def solution(nums):
    mon = {}
    for i in range(len(nums)):
        if nums[i] in mon:
            mon[nums[i]] += 1
        else:
            mon[nums[i]] = 1
    answer = min(len(nums) // 2, len(mon))
    return answer
