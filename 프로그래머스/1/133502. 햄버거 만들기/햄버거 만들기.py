def solution(ingredient):
    stack = []
    answer = 0
    
    for i in ingredient:
        stack.append(i)
        
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            for i in range(4):
                stack.pop()
            answer += 1
    
    return answer