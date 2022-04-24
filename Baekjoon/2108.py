from collections import Counter
import sys
input = sys.stdin.readline


def mode(num_list):
    cnt_list = Counter(num_list)
    modes = cnt_list.most_common(2)
    if len(modes) == 1:
        print(modes[0][0])
    else:
        if modes[0][1] == modes[1][1]:
            print(modes[1][0])
        else:
            print(modes[0][0])


N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
print(round(sum(numbers) / N))
print(numbers[N // 2])
mode(numbers)
print(numbers[-1] - numbers[0])
