# quick sort
import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))


def quick_sort(array, start, end):
    if start >= end:
        return
    curr = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[curr]:
            left += 1
        while right > start and array[right] >= array[curr]:
            right -= 1
        if left > right:
            array[right], array[curr] = array[curr], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(arr, 0, len(arr) - 1)
print(*arr, sep=' ')
