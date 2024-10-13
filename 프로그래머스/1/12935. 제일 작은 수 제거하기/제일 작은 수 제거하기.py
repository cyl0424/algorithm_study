def solution(arr):
    answer = []
    print(min(arr))
    if (len(arr) == 1):
        answer.append(-1)
    else:
        arr.remove(min(arr))
        answer = arr
    return answer