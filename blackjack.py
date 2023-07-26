import random
#TODOS:
# 1. Deal Card - 2 random; for both.   DONE
# 2. Check if both the player have more than 21 Done
# 3. If not, Player has bet/stand options   Done
# 4. If bet - Player takes a new card Once, Check if it's more than 21.  
# 5. If not, give option of bet/stand. 
# 6. If stand play the card, if bet draw again.
# 7. When stand, sum Players card first and then Cpu's sum. If cpu's sum < 17 draw again and again.
# 8. When done, check all the sum if player > cpu <<= 21 player wins. Append score.
def deal_card(): # 1 draw
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    return random.choice(cards)

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0 #Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1) #For Ace
    return sum(cards)

def compare(player_score, dealer_score, game_over):
    if player_score > dealer_score and player_score <= 21:
        print(f"Player Cards : {player_score} and Dealer Cards: {dealer_score}")
        print("Player wins wins")
        game_over = True
    elif dealer_score > player_score and dealer_score <= 21:
        print(f"Player Cards : {player_score} and Dealer Cards: {dealer_score}")
        print("Player wins wins")
        game_over = True
        
    return game_over

def play_game():
    print("\n\nGAME START!! !! !!")
    #Setting default card as empty
    dealer_card = []
    player_card = []
    game_over = False
    
    for _ in range(2):
        dealer_card.append(deal_card())
        player_card.append(deal_card())
        
    print("Player Cards: ", player_card)
    print("Dealer cards: ", dealer_card_hidden := dealer_card[:-1] + ["*"])
    
    while not game_over:
        player_score = calc_score(player_card)
        dealer_score = calc_score(dealer_card)
        if player_score > 21 or dealer_score == 0:
            print(f"Player Cards : {player_score} and Dealer Cards: {dealer_score}")
            print("Dealer wins")
            game_over = True
        elif player_score == 0 or dealer_score > 21:
            print(f"Player Cards : {player_score} score: and Dealer Cards: {dealer_score}")
            print("Player wins wins")
            game_over = True
        else:
            choice = int(input("Your Choice: 1.Bet 2.Stand: "))
            if choice == 1: 
                player_card.append(deal_card()) # Get another card for bet
                player_score = calc_score(player_card)
                print(f"You took a card. Now: {player_card} -> {player_score}")
                if player_score > 21:
                    print(f"Player Cards :{player_card} -> {player_score} and Dealer Cards:{dealer_card} -> {dealer_score}")
                    print("Dealer wins")
                    game_over = True
            elif choice ==2:
                print("You Choose Stand")
                print(f"Player Card: {player_card}")
                while dealer_score < 17 or not dealer_score > 17: #Stand and Dealer cards <17
                    print("Dealer Taking cards till 17")
                    print(dealer_card)
                    dealer_card.append(deal_card())
                    dealer_score = calc_score(dealer_card)
                    if dealer_score > 21:
                        print(f"Player Cards : {player_score} and Dealer Cards: {dealer_score}")
                        print("Player wins wins")
                        game_over = True
                print(f"Dealer Card: {dealer_card}")
                compare(player_score, dealer_score, game_over)
                
    print("Player Score: ", player_score)
    continue_game = int(input("Continue? 1. Yes : "))
    if continue_game == 1:
        play_game()
play_game()