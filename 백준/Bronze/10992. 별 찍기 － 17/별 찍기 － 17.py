num = int(input())

print(" " * (num-1) + "*")

if num != 1:
    for i in range(2, num):
        print(" " * (num - i) + "*" + " " * (2*(i-1)-1) + "*")
    print("*" * (2*num -1))