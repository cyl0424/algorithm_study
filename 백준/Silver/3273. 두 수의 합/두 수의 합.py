import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

left, right = 0, n-1
answer = 0

while left < right:
    tmp = nums[left] + nums[right]
    if tmp == x:
        answer += 1
        left += 1
    elif tmp > x:
        right -= 1
    else:
        left += 1

print(answer)