def solution(n, times):
    low = 1
    high = 1e18
    while low <= high:
        mid = (low + high) // 2
        cnt = 0
        for i in range(len(times)):
            cnt += mid // times[i]
        if cnt >= n:
            high = mid - 1
        elif cnt < n:
            low = mid + 1
    return low
