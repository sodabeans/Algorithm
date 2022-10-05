def solution(n):
    answer = 0
    fib = [0] * (n + 1)
    fib[1] = 1
    
    for idx in range(2, n + 1):
        fib[idx] = (fib[idx - 1] + fib[idx - 2]) % 1234567
    
    return fib[-1]
    
