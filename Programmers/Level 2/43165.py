def dfs(idx, curr, numbers, target):
    if idx == len(numbers):
        if curr == target:
            return 1
        else:
            return 0
    return dfs(idx + 1, curr + numbers[idx], numbers, target) + dfs(idx + 1, curr - numbers[idx], numbers, target)
    

def solution(numbers, target):
    return dfs(0, 0, numbers, target)
