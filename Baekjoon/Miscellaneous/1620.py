import sys
input = sys.stdin.readline

N, M = map(int, input().split())

number_key_dict = dict()

for i in range(1, N+1):
    pokemon_name = input().strip('\n')
    number_key_dict[i] = pokemon_name

# https://seong6496.tistory.com/72
# key와 value의 위치를 바꿔주기
name_key_dict = dict(map(reversed, number_key_dict.items()))

for _ in range(M):
    search = input().strip('\n')
    if search.isnumeric():
        print(number_key_dict[int(search)])
    else:
        print(name_key_dict[search])
