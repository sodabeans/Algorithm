from collections import Counter
import sys
input = sys.stdin.readline


def mode(num_list):
    modes = list()
    cnt_list = Counter(num_list)
    cnt = cnt_list.most_common(1)[0][1]
    for c in cnt_list:
        if num_list.count(c) == cnt:
            modes.append(c)
    if len(modes) > 1:
        cnt = modes[1]
    print(cnt)


N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
print(round(sum(numbers) / N))
print(numbers[N // 2])
mode(numbers)
print(numbers[-1] - numbers[0])
