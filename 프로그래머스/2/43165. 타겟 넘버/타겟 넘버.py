# BFS
def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for num in numbers:
        tmp = []
        for leave in leaves:
            tmp.append(leave + num)
            tmp.append(leave - num)
        leaves = tmp
    
    answer = leaves.count(target)
    
    return answer

# DFS
# def solution(numbers, target):
#     answer = DFS(numbers, target, 0)
#     return answer

# def DFS(numbers, target, depth):
#     answer = 0
#     if depth == len(numbers):
#         if sum(numbers) == target:
#             return 1
#         else:
#             return 0
#     else:
#         answer += DFS(numbers, target, depth + 1)
#         numbers[depth] *= -1
#         answer += DFS(numbers, target, depth + 1)
        
#         return answer