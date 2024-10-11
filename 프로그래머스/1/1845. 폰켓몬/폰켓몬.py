def solution(nums):
    answer = 0
    mid = len(nums) // 2
    newSet = set(nums)
    if (len(newSet) < mid):
        return len(newSet)
    else:
        return mid
    return answer