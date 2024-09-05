n = int(input())
nums = []

for _ in range(n):
    nums += list(map(int, input().split()))
    nums.sort(reverse=True)
    if len(nums) > n :
        nums = nums[:n]

print(nums[-1])
    