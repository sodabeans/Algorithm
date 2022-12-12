def solution(citations):
    answer = 0
    citations.sort()
    for idx in range(len(citations) - 1, -1, -1):
        curr = 0
        for c in citations:
            if c >= idx + 1:
                curr += 1
        if curr >= idx + 1:
            answer = max(answer, idx + 1)
            break

    return answer
