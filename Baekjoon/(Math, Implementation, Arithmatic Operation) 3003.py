import sys
input = sys.stdin.readline

king, queen, rook, bishop, knight, pawn = map(int, input().split())
print(f'{1 - king} {1 - queen} {2 - rook} {2 - bishop} {2 - knight} {8 - pawn}')
