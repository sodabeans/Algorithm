import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    animal_sound = list()
    test_case = input().rstrip().split()

    while True:
        animals = input().rstrip()
        if animals == 'what does the fox say?':
            break
        tmp = animals.split()
        animal_sound.append(tmp[-1])

    print(' '.join([t for t in test_case if t not in animal_sound]))
