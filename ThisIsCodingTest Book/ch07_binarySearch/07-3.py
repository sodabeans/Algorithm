import sys
input = sys.stdin.readline

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
answer = -1
start = 0
end = n - 1

while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
        answer = mid
        break
    elif arr[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

if answer == -1:
    print("target not found")
else:
    print(answer + 1)
