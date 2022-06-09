result = [0]*10

a = int(input())
b = int(input())
c = int(input())

mul = a*b*c

while mul > 0:
    result[mul%10] += 1
    mul = mul//10
    
for i in range(10):
    print(result[i])