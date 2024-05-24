def solution(n):
    ans = 0
    while n:
        remainder = n % 2
        if remainder == 0:
            n = n // 2
        else:
            n -= remainder
            ans += remainder

    return ans
