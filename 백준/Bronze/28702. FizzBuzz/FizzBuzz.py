a = input()
b = input()
c = input()

next = 0

if (a not in "FizzBuzz"):
    next = int(a)+3
elif(b not in "FizzBuzz"):
    next = int(b)+2
elif(c not in "FizzBuzz"):
    next = int(c)+1

if (next % 3 == 0 and next % 5 == 0):
    print("FizzBuzz")
elif (next % 3 == 0):
    print("Fizz")
elif (next % 5 == 0):
    print("Buzz")
else:
    print(next)