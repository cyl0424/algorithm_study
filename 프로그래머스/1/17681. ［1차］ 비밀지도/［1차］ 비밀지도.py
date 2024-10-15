def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        binaryNum1 = bin(arr1[i])[2:]
        arr1[i] = '0' * (n-len(binaryNum1)) + binaryNum1
        
        binaryNum2 = bin(arr2[i])[2:]
        arr2[i] = '0' * (n-len(binaryNum2)) + binaryNum2
    
    for a, b in zip(arr1, arr2):
        tmp = ''
        for i in range(n):
            if a[i] == '1' or b[i] == '1':
                tmp += '#'
            else:
                tmp += ' '
        
        answer.append(tmp)
    
    return answer