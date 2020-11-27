import sys

def collatz(number):
        result = 0
        if number % 2 == 0:
            print("The number you've choosen is EVEN: ", number)
            print("number // 2: ", number // 2)
            result = number // 2
        elif number % 2 == 1:
            print("The number you've choosen is ODD: ", number)
            print("3 * number + 1: ", 3 * number + 1)
            result = 3 * number + 1
            
        while result == 1:
            print(result)
            sys.exit()
            
        while result != 1:
            number = result
            return collatz(number)
         
print("Choose a number: ", end='')             
try:
    number = int(input())
    collatz(number)
except ValueError:
    print("\nPut a number....")

