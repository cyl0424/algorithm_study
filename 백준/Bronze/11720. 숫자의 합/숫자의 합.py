num = int(input())

numList = input()

sum = 0

if len(numList) == num :
  for i in range(num) :
    sum += int(numList[i])
  
  print(sum)