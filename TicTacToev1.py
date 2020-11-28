import random
import sys

#Values for the TicTacToe
values = [' ' for x in range(9)]

#Initial Variables
player_choice = ''
AI_choice = ''
first_turn = 0
starting_player = ''

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
def player_choice_function():
    global player_choice
    global AI_choice 
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
        #Updated player_choice and AI_choice varibales
        player_choice = "X"
        AI_choice = "0" 
    if choice == 2:
        #Updated player_choice and AI_choice varibales
        player_choice = "0"
        AI_choice = "X"  
    if choice == 3:
        #Sys.exit yeah...
        sys.exit()
        
     #Calling turn_start() for first random pick
    turn_start()    


#Function for random 1st pick
def turn_start():
    global first_turn
    global starting_player
    #Random draw
    randomStart = random.randint(0,1)
    #setting up starting player inorder to enable next turn for AI and player
    if randomStart == 0:
        starting_player = 'X'
    if randomStart == 1:
        starting_player = '0'
        
    #Checking which player got 1st turn
    if player_choice == starting_player:   
        print("Your Turn is 1st: ")
        first_turn = 1
        #get_player_input = player turn
        get_player_input()
    elif AI_choice == starting_player:
        
        print("AI turn's first")
        #AI_input = AI turn
        AI_input()


#Function for next turn and comes only if turn_start() is held once
def next_turn():
    #first turn is setted up on the way in order to it can switch to 1 and 0 and turn happens
    if first_turn == 1:
        get_player_input()
    if first_turn == 0:
        AI_input()


#Player Turn:
def get_player_input():
    global first_turn
    print("Your turn: ", end='')
    #Setting up which box u want to put ur value
    while True:
        try:
            get_player_input = int(input())
            #Limiting 1-9 for the box
            if get_player_input < 1 or get_player_input > 9:
                print("Wrong Input! Try again.")
                continue
            #updating position for list
            get_player_input = get_player_input - 1 
            
            get_values = values[get_player_input]
            #checking if its filled or not
            if get_values != ' ':
                print("Places already filled. Try again!!")
                return
 
        except ValueError:
            print("Give a digit!")
            return
        
        break 
    first_turn = 0
    get_process(get_player_input, player_choice)  


#AI Turn:
def AI_input():
    global first_turn
    while True:
        #Random pick from it..XD
        get_player_input = random.randint(0,8)
        get_values = values[get_player_input]
        #If it's filled or not
        if get_values != ' ':
            return
        break
    print("AI chooses...")
    first_turn = 1
    get_process(get_player_input, AI_choice)


#Just a process needed to made before in order to re-arrange and warp up everythin so that I dont face problem
def get_process(input, cur_player):
    cur_choice = input
    process_input(cur_player, cur_choice)   


#The main function to check if the values are matched or not...if matched its a win...
#If it didn't match it calls the next_turn()
def process_input(cur_player, cur_choice):
    values[cur_choice] = cur_player
    print_tic_tac_toe(values)
    
    while True:
        if values[6] == values[7] == values[8] != ' ': # across the top
            print("\nGame Over.\n")                            
            main()
            break
        elif values[3] == values[4] == values[5] != ' ': # across the middle
            print("\nGame Over.\n")
            main()              
            break
        elif values[0] == values[1] == values[2] != ' ': # across the bottom
            print("\nGame Over.\n")
            main()
            break             
        elif values[0] == values[3] == values[6] != ' ': # down the left side
            print("\nGame Over.\n")
            main()
            break           
        elif values[1] == values[4] == values[7] != ' ': # down the middle
            print("\nGame Over.\n")
            main()
            break
        elif values[2] == values[5] == values[8] != ' ': # down the right side
            print("\nGame Over.\n")
            main()
            break       
        elif values[6] == values[4] == values[2] != ' ': # diagonal
            print("\nGame Over.\n")
            main()
            break
        elif values[0] == values[4] == values[8] != ' ': # diagonal
            print("\nGame Over.\n")
            main()
            break
        else:
            next_turn()


def main():
    
    #reset
    values = [' ' for x in range(9)]
    player_choice = ''
    AI_choice = ''
    first_turn = 0
    starting_player = ''
    
    #1st: Player Choice
    #2nd : Turn Start (Randomizing who will do first) (Done only once at the beginning)
    #2nd (If Turn Start is done once) : Next Turn
    #3rd : get_player_input = player input and AI_input = AI input....the one choosen at next turn comes his executed
    #4th : get_process (Just added it if i ever need to organize anything...)
    #5th : process_input (does the printing of print_tic_tac_toe(values) as well as checks if its a win or not...if not it returns to next_turn) 
    
    player_choice_function()
main()
