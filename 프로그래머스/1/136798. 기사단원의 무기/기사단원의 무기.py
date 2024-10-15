def solution(number, limit, power):
    answer = 0
    nums = []
    
    for n in range(1, number+1):
        cnt = 0
        
        if n == 1:
            nums.append(1)
        else:
            if n **0.5 == int(n**0.5):
                cnt -= 1  
                
            for i in range(1, int(n**0.5)+1):
                if n % i == 0:
                    cnt += 2
            
            if cnt <= limit:
                nums.append(cnt)
            elif cnt > limit:
                nums.append(power)
    
    answer = sum(nums)
    return answer