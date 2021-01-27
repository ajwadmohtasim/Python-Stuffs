"""
HANGMAN_v1                      //27 Jan, 2021



A simple guessing game, where you are given to guess a word randomly and 6 lives. Guess the correct word or for each
wrong guess your lives gets dedcuted
"""

import random


scoreboard_stats = {"win": 0, "lose": 0}

hangman_picture = [  
                   #full state
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   #5 tries left
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   #4 tries left
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   #3 tries left
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   #2 tries left
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   #1 tries left
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   #over
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]

words = ["apple", "ball", "hat", "dog", "physics", "chemistry", "mathematics",
         "cat", "burger", "pizza", "hamburger", "college"] #words list

word_dict = {"lives" : 6}
word_dict_reset = {"lives" : 6}

#word select -  shall only be called once for each game
def word_select(words):
    word = random.choice(words).upper() #Random word select
    #Count how many hints can be given based upon the word. 
    #40% of total world length as hint tries. (10 words - 4 hints)
    word_length = len(word)
    word_hint = round(word_length * .4)
    #password like hidden words
    password = "*" * word_length
    #update word dictionary for datas
    word_dict["word"] = word
    word_dict["word_length"]  = str(word_length)
    word_dict["word_hint"] = str(word_hint)
    word_dict["password"] = password
    word_dict["hint"] = []
    word_dict["hangman_state"] = hangman_picture[0]
    
    #word list - for updating word and others
    split_word = list(word_dict["word"])
    word_dict["split_word"] = split_word
    return
#Hint - reveals any of the word, based on total word hints
def hint_system(word_dict):
    hint = int(word_dict["word_hint"]) #Hint Count
    if hint != 0:
        hint = hint - 1
        word_dict["word_hint"] = str(hint)
    else:
        print("-------------------------------------------")
        print("NO HINT AVAILABLE")
        print("-------------------------------------------")
        get_input()

    while True:
        random_split_word = random.choice(word_dict["split_word"])
        if random_split_word == "*": #avoid giving * as hint
            return
        if random_split_word in word_dict["hint"]: #avoid giving words that's already given as hint
            return
        word_dict["hint"].append(random_split_word)
        print("-------------------------------------------")
        print("There is a chracter: ", random_split_word, " in the word")
        print("-------------------------------------------")
        break
    get_input()
        

def get_input():
    print("")
    print("\t\t", word_dict["hangman_state"])
    print("#################--------------", end="")
    print("\t\t", "WIN: ", scoreboard_stats["win"], "LOSE: ", scoreboard_stats["lose"])
    print("THE WORD IS         : " + word_dict["password"])
    print("Total Hint Available: " + word_dict["word_hint"])
    print("Word Length         : " + word_dict["word_length"])
    print("What do you want to do?")
    print("#################--------------")
    print("")
    print("Guess the word? (1 = hint) >", end="")
    
    while True: #answer input; either a single guess/the whole word guess
        answer_input = str(input()).upper() 
        if answer_input == "1":
            hint_system(word_dict)
        elif answer_input.isalpha() and len(answer_input) == 1: #single guess
            verify(answer_input)
        elif answer_input.isalpha() and len(answer_input) == int(word_dict["word_length"]):
            verify_whole(answer_input)
        else:
            print("-------------------------------------------")
            print("Not a vaild guess (Either guess a word or the whole word)..")
            get_input()
        break
    
#Verifying whole guessed word.
def verify_whole(answer_input):
    lives = word_dict["lives"]
    if answer_input == word_dict["word"]:
        print("--------------------###-------------------")
        print("Congrats!! You Guessed the correct word!!")
        print("--------------------###-------------------")
        scoreboard_stats["win"] = scoreboard_stats["win"] + 1
        main()
    else:
        print("Not the correct guess")
        lives = lives -1
        
    if lives != 0: #updating live numbers
        word_dict["lives"] = lives
        hangman_state(lives)
    else:
        hangman_state(lives)
        
#Verifying single guessed word.
def verify(answer_input):
    lives = word_dict["lives"]

    if answer_input in word_dict["split_word"]: #Checking if the answer input matches the words 
        print("--------------------000-------------------")
        print("The word ", answer_input, " is present in the word!")
        update_word(answer_input)
        
    else:   #deduct lives
        print("--------------------000-------------------")
        print("The word ", answer_input, "is not present in the word!")
        lives = lives - 1

    if lives != 0: #updating live numbers
        word_dict["lives"] = lives
        hangman_state(lives)
    else:
        hangman_state(lives)
        

#updates the word in the "_password_" taking matched answer input
def update_word(answer_input):
    current_word_list = word_dict["split_word"] #Existing list of word
    password_list = list(word_dict["password"]) #Storing password in a list format
    word_index = current_word_list.index(answer_input) #getting which index matches answer_input
    
    #replacing word with updated word- so that it sets the "*" with the updated word taken as input.
    if answer_input not in password_list[word_index] and answer_input != "*":
        password_list[word_index] = answer_input
    else:
        print("###-------------------")
        print("The word is already showed")
    
    #replacing password word with the updated word
    updated_word = ""
    for words in password_list:
        updated_word += words
    
    word_dict["password"] = updated_word
    
    if word_dict["password"] != word_dict["word"]:
        get_input()
    else:
        print("--------------------###-------------------")
        print("Congrats!! You guessed the correct word!!")
        print("--------------------###-------------------")
        win = scoreboard_stats["win"]
        scoreboard_stats["win"] = win + 1
        print(scoreboard_stats["win"])
        main()


def hangman_state(lives):
    if lives == 6:
        word_dict["hangman_state"] = hangman_picture[0]
    elif lives == 5:
        word_dict["hangman_state"] = hangman_picture[1]
    elif lives == 4:
        word_dict["hangman_state"] = hangman_picture[2]
    elif lives == 3:
        word_dict["hangman_state"] = hangman_picture[3]
    elif lives == 2:
        word_dict["hangman_state"] = hangman_picture[4]
    elif lives == 1:
        word_dict["hangman_state"] = hangman_picture[5]
    elif lives == 0:
        word_dict["hangman_state"] = hangman_picture[6]
        game_over()
    get_input()

def game_over():
    print("############")
    print("GAME OVER...")
    print("############")
    scoreboard_stats["lose"] = scoreboard_stats["lose"] + 1
    print("lose: ", scoreboard_stats["lose"])
    main()

def main():
    word_dict["lives"] = 6
    word_select(words)
    get_input()
main()