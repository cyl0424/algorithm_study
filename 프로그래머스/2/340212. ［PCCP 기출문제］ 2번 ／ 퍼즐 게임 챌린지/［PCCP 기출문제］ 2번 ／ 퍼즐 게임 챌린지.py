def solution(diffs, times, limit):
    def can_solve_with_level(level):
        total_time = 0
        
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i-1] if i > 0 else 0
            
            if diff <= level:
                solve_time = time_cur
            else:
                solve_time = (diff - level) * (time_cur + time_prev) + time_cur
            
            total_time += solve_time
            
            if total_time > limit:
                return False
        
        return total_time <= limit
    

    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_solve_with_level(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer
