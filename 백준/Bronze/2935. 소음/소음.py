a = int(input())
oper = input()
b = int(input())

res = 0

operations = {
    '*': a * b,
    '+': a + b
}
    
print(operations[oper])