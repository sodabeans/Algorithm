def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    arr2_transformed = []
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            curr = []
            for k in range(len(arr2)):
                # print(f'i: {i} j: {j} k: {k}')
                curr = arr1[i][k] * arr2[k][j]
                answer[i][j] += curr
    return answer
