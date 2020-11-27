import random, sys

#Values for the TicTacToe
values = [' ' for x in range(9)]

#Initial Variables
playerChoice = ''
AIchoice = ''
firstTurn = 0
startingPlayer = ''

#Starting with name....
print("What's your name? : ", end='')
player_name = str(input())

#Printing Tic Tac Toe Screen getting values from the values list
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

#Player choice: Do you want to take X or 0...
def player_choice():
    
    global playerChoice
    global AIchoice
    
    print("Turn to choose for ", player_name)

    while True:
        
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
        
        try:
            #Setting up 1-3 options
            choice = int(input())
            if choice < 1 or choice > 3:
                print("Wrong Input! Try again.")
                continue
            
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
        break
    
    if choice == 1:
        #Updated playerChoice and AIchoice varibales
        playerChoice = "X"
        AIchoice = "0"
    
    if choice == 2:
        #Updated playerChoice and AIchoice varibales
        playerChoice = "0"
        AIchoice = "X"
        
    if choice == 3:
        #Sys.exit yeah...
        sys.exit()
        
     #Calling turn_start() for first random pick
    turn_start()    


#Function for random 1st pick
def turn_start():
    global firstTurn
    global startingPlayer
    
    #Random draw
    randomStart = random.randint(0,1)
    #
    #setting up starting player inorder to enable next turn for AI and player
    if randomStart == 0:
        startingPlayer = 'X'
    if randomStart == 1:
        startingPlayer = '0'
    
    #Checking which player got 1st turn
    if playerChoice == startingPlayer:
        
        print("Your Turn is 1st: ")
        firstTurn = 1
        #get_input = player turn
        get_input()
        
    elif AIchoice == startingPlayer:
        
        print("AI turn's first")
        #AI_input = AI turn
        AI_input()

#Function for next turn and comes only if turn_start() is held once
def next_turn():
    
    #first turn is setted up on the way in order to it can switch to 1 and 0 and turn happens
    if firstTurn == 1:
        get_input()
    if firstTurn == 0:
        AI_input()

#Player Turn:
def get_input():
    
    global firstTurn
    
    print("Your turn: ", end='')
    
    firstTurn = 0
    #Setting up which box u want to put ur value
    while True:
        try:
            getInput = int(input())
            #Limiting 1-9 for the box
            if getInput < 1 or getInput > 9:
                print("Wrong Input! Try again.")
                continue
            #updating position for list
            getInput = getInput - 1 
            
            getValues = values[getInput]
            #checking if its filled or not
            if getValues != ' ':
                print("Places already filled. Try again!!")
                return
 
        except ValueError:
            print("Give a digit!")
            return
        
        break 

    get_process(getInput, playerChoice)  

#AI Turn:
def AI_input():
    
    global firstTurn
    
    firstTurn = 1
    
    print("AI chooses...")
    while True:
        #Random pick from it..XD
        getInput = random.randint(0,9)

        getValues = values[getInput]

        #If it's filled or not
        if getValues != ' ':
            return
        break
    get_process(getInput, AIchoice)

#Just a process needed to made before in order to re-arrange and warp up everythin so that I dont face problem
def get_process(input, cur_player):
    cur_choice = input
    process_input(cur_player, cur_choice)   

#The main function to check if the values are matched or not...if matched its a win...
#If it didn't match it calls the next_turn()
def process_input(cur_player, cur_choice):
    
    values[cur_choice] = cur_player
    print_tic_tac_toe(values)
    
    #a list in order to check if the current list is matched or not
    # Lame way is that give all the possible which will make a huge mess in this list
    # So keeping this at this moment...no one will win.
    soln = [
        [cur_choice, cur_choice, cur_choice, ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ' ,cur_choice, cur_choice, cur_choice, ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', cur_choice, cur_choice, cur_choice],
        [cur_choice, ' ', ' ', cur_choice, ' ', ' ', cur_choice, ' ', ' '],
        [' ', cur_choice, ' ', ' ', cur_choice, ' ', ' ', cur_choice, ' '],
        [' ', ' ', cur_choice, ' ', ' ', cur_choice, ' ', ' ', cur_choice],
        [cur_choice, ' ', ' ', ' ', cur_choice, ' ', ' ', ' ', cur_choice],
        [' ', ' ', cur_choice, ' ', cur_choice, ' ', cur_choice, ' ', ' ']
    ]
    
    #Not yet implemented... ignore
    soln2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]
    #process 2
    #Not yet implemented 
    
    #process 1 (Didn't work...probably due to the list having ' '  and not AI values)
    if any(list == values for list in soln): 
        print("You have won!!!") 
    else:
        #Calling next_turn() as none of the above soln matched...so no win >.>
        next_turn()

def main():
    #1st: Player Choice
    #2nd : Turn Start (Randomizing who will do first) (Done only once at the beginning)
    #2nd (If Turn Start is done once) : Next Turn
    #3rd : get_input = player input and AI_input = AI input....the one choosen at next turn comes his executed
    #4th : get_process (Just added it if i ever need to organize anything...)
    #5th : process_input (does the printing of print_tic_tac_toe(values) as well as checks if its a win or not...if not it returns to next_turn) 
    while True:
        player_choice()
        break   
main()