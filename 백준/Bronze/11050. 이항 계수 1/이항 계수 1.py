def factorial(n):
    if n <= 0:
        return 1

    else:
        return n * factorial(n-1)

def nCr(n, r):
    if r > (n//2):
        r = n-r
    result = factorial(n)/(factorial(r)*factorial(n-r))
    return int(result)

a, b = map(int, input().split())
print(nCr(a,b))

