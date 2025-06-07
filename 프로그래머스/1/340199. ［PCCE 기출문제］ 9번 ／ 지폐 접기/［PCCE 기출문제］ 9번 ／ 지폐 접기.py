def solution(wallet, bill):
    answer = 0
    wallet.sort(reverse = True)
    bill.sort(reverse = True)
    
    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        bill[0] //= 2
        answer += 1
        
        bill.sort(reverse = True)
        
    return answer