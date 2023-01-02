from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    entry = input().rstrip().split(" ")
    if entry[0] == 'push':
        queue.append(int(entry[1]))
    elif entry[0] == 'pop':
        if len(queue):
            print(queue.popleft())
        else:
            print("-1")
    elif entry[0] == 'size':
        print(len(queue))
    elif entry[0] == 'empty':
        if len(queue):
            print("0")
        else:
            print("1")
    elif entry[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print("-1")
    elif entry[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print("-1")
