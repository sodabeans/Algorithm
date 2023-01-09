from itertools import combinations
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
characters = list(map(str, input().split()))
characters.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
passwords = list(combinations(characters, L))

for word in passwords:
    cnt_v = 0
    cnt_c = 0
    for c in word:
        if c in vowels:
            cnt_v += 1
        else:
            cnt_c += 1
    if cnt_v >= 1 and cnt_c >= 2:
        print("".join(word))
