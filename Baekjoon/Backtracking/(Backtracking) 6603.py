import sys
input = sys.stdin.readline


def select(numbers, answer):
    if len(answer) == 6:
        print(" ".join(map(str, answer)))
        answer = []
        return
    for idx in range(len(numbers)):
        if(answer and answer[-1] > numbers[idx]) or numbers[idx] in answer:
            continue
        answer.append(numbers[idx])
        select(numbers, answer)
        answer.pop()


while True:
    S = list(map(int, input().split()))
    k = S.pop(0)
    ans = []
    if k == 0:
        break
    select(S, ans)
    print()
