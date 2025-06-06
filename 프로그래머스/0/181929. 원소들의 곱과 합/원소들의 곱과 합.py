def solution(num_list):
    add = sum(num_list)
    mult = 1
    
    for num in num_list:
        mult *= num
    
    if mult < add ** 2:
        return 1
    return 0