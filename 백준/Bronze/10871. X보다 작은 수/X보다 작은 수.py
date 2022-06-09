cnt, num = map(int, input().split())
intList = list(map(int, input().split()))
   
for i in range(cnt):
    if intList[i] < num:
        print(intList[i], end = " ")