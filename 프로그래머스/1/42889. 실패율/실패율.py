def solution(N, stages):
    answer = []
    status = {}
    
    total = len(stages)
    
    for i in range(1, N+1):
        cnt = stages.count(i)
        percentage = 0
        
        if total > 0:
            percentage = cnt / total
            total -= cnt
        
        status[i] = percentage
    
    status = dict(sorted(status.items(), key = lambda item : (-item[1], item[0])))
    
    return list(status.keys())