import sys
input = sys.stdin.readline

total_eqn = list(input().rstrip().split('-'))
partial_eqn = [sum(map(int, part.split("+"))) for part in total_eqn]
ans = partial_eqn[0] - sum(partial_eqn[1:])
print(ans)
