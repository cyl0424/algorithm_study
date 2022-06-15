students = list(range(1,31))

for _ in range(28):
    num = int(input())
    students.remove(num)

for i in students:
    print(i)