# 큰 수의 법칙
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
cnt = M // (K + 1)
remainder = M % (K + 1)
print(cnt * (nums[0] * K + nums[1]) + remainder * nums[0])
