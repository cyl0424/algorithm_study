import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
sorted_num_set = sorted(list(set(nums)))
num_dict = defaultdict(int)

for i, num in enumerate(sorted_num_set):
    num_dict[num] = i

result = []

for num in nums:
    result.append(num_dict[num])

print(*result)