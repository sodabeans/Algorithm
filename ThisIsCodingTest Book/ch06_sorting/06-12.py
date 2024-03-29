import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

arr_A.sort()
arr_B.sort(reverse=True)

for i in range(K):
    if arr_A[i] >= arr_B[i]:
        break
    arr_A[i], arr_B[i] = arr_B[i], arr_A[i]

print(sum(arr_A))
