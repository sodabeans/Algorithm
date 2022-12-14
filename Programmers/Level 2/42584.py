def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        curr = prices[i]
        for j in range(i + 1, len(prices)):
            if prices[j] >= curr:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)

    return answer
