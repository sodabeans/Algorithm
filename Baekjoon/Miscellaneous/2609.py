import math
import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())

print(math.gcd(num1, num2))
print(math.lcm(num1, num2))