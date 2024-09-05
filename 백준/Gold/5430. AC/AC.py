def execute_AC(p, arr):
    is_reversed = False
    front = 0
    rear = 0

    for cmd in p:
        if cmd == 'R':
            is_reversed = not is_reversed

        elif cmd == 'D':
            if is_reversed:
                rear += 1
            else:
                front += 1               

    if front + rear > len(arr):
        return "error"

    result = arr[front:len(arr)-rear]    

    if is_reversed:
        result = result[::-1]

    return "[" + ",".join(map(str, result)) + "]"

def main():
    import sys
    input = sys.stdin.read
    
    data = input().strip().split('\n')    

    T = int(data[0])

    index = 1
    results = []

    for _ in range(T):
        p = data[index].strip()
        n = int(data[index + 1].strip())

        if n == 0:
            arr = []

        else:
            arr = list(map(int, data[index + 2].strip()[1:-1].split(',')))

        index += 3

        result = execute_AC(p, arr)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()