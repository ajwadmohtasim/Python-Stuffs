import random

def main():

    print("Welcome to random number guessing game: ")
    print("Think a number, and give me a range too.")
    
    highestRange = 0
    lowestRange = 0
    
    while True:
        
        try:
            print("What is the highest range?: ", end='')
            highestRange = int(input())
        except ValueError:
            print("\nPut a number....")
            continue
        break
    
    while True:
        try:
            print("What is the lowest range?: ", end='')
            lowestRange = int(input())
        except ValueError:
            print("\nPut a number....")
            continue
        break
    
    print(f"So the range is {highestRange} - {lowestRange}")
    while True:
        
        def guess(highestRange, lowestRange):
            guessNum = (highestRange + lowestRange) / 2
            guessNum = round(guessNum)
            
            print( f'Is the number {guessNum}? (Is the guess (C)orrect or (I)ncorrect?')
            getAns = str(input())
            
            correctAns = [
                "Oh wow! I guessed it right!!\n\n",
                "I am the best, isn't it!\n\n",
                "That was easy....XD\n\n"
            ]
            
            if getAns == 'C':
                print(random.choice(correctAns))
                return main()
            
            elif getAns == 'I':
                print('Okay...Is it (G)reater or (L)ower than this?')
                getAns = str(input())
                
                if getAns == 'G' or "L":
                    
                    if getAns == 'G':
                        print("so it is higher...Okay!")
                        lowestRange = guessNum
                        guess(highestRange, lowestRange)
                        
                    elif getAns ==  'L':
                        print("So it is lower...Okay!")
                        highestRange = guessNum
                        guess(highestRange, lowestRange)
                        
                elif getAns != 'G' or 'L':
                    print("print either G or L")
                    
        guess(highestRange, lowestRange)
        
main()