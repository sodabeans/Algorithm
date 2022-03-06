def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

for _ in range(int(input())):
    sum = 0
    case = list(map(int, input().split()))
    length = case.pop(0)
    case.sort()
    for j in range(length):
        for k in range(j):
            sum = sum + gcd(case[j], case[k])
    print(sum)