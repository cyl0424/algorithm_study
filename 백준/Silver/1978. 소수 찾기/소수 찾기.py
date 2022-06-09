import sys, math

def is_prime(x) :
    if x < 2 :
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0 :
            return False
    return True
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
for i in arr :
    if is_prime(i) :
        result +=1 

print(result)