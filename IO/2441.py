# 별 찍기 N개부터 1개까지 찍기 오른쪽 정렬

num = int(input())

for i in range(num, 0, -1):
  print(' ' * (num - i) + '*' * i)
