import random, sys

#Variables
wins = 0
lose = 0
ties = 0

print("ROCK PAPER SCISSORS!!!!!")
#Main Game Loop
while True:
    print('%s wins, %s lose, %s ties' % (wins,lose,ties))
    while True: #The player input
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quit the programme
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #break out of the plauer input loop
        print('Type one of  r, p ,s or q')
        
    #Display player choice 
    if playerMove == 'r':
        print("ROCK versus...")
    elif playerMove == 'p':
        print("PAPER versus...")
    elif playerMove == 's':
        print("SCISSORS versus...")
    
    #Display what the computer choose:
    randomNumber = random.randint(1, 3)
    computerMove = ''
    
    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove = 's'
        print("SCISSORS")
        
    #Display the result
    if playerMove == computerMove:
        print("It's a tie")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 'p':
        print("You lose!")
        lose = lose + 1
    elif playerMove == "r" and computerMove == 's':
        print("You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == 's':
        print("You lose!")
        lose = lose + 1
    elif playerMove == "p" and computerMove == 'r':
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == 'p':
        print("You win!")
        wins = wins + 1  
    elif playerMove == "s" and computerMove == 'r':
        print("You Lose!")
        lose = lose + 1  
        
        