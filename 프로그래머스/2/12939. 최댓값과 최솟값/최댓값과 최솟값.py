def solution(s):
    nums = list(map(int, s.split(" ")))
    print(nums)
    answer = str(min(nums)) + " " + str(max(nums))
    return answer