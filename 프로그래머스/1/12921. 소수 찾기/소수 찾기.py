def solution(n):
    answer = 0
    nums = set(range(2, n+1))
    
    for i in range(2, int(n**0.5)+1):
        if i in nums:
            nums -= set(range(i*2, n+1, i))
    
    answer = len(nums)
    return answer