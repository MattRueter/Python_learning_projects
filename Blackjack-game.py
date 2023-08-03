import random

'''
##Playing the game.
print("Here are your cards.")
##Deal cards here
print(input("Do you want another card?"))
##yes ? THEN deal a third card.
##no ? THEN don't deal a third card.


##Automated game.
print("Here are your cards")
print(value_of_card("4"), value_of_card("10"))
print("Would you like a third card?")
##decide YES or NO based on if value_of_card(card_one) and value_of_card(card_two) <=10
##if current_value is between 11 and 14 YES
##if current_value is between 15 and 18 random choice between YES and NO
##if current_value is 19-20 NO.
## * the YES or NO code can be wrapped in a function which can be toggle for riskier or less riskier behaviour.
print("value of third card")
##print end game logic
    ##END GAME LOGIC
    ## print third card
    ## add up all three cards (If third card is ACE run value of ace logic)
    ## print total 
    ## print congrats or sorry message.
'''

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

##Functions for game play.----------------------------------------------------------------------------

def deal_card(): 
    """Randomly chooses a single card from cards list.
    return: str -> representing one of the cards from 2-K and A.
    """
    index = random.randint(0,len(cards)-1)
    card = cards[index]
    return card

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value = 0
    face_cards = ["K", "Q", "J"]
    if(card in face_cards):
        value = 10
    elif(card == "A"):
        value = 1
    else:
        value = int(card)
    return value

def ace_in_first_hand(card_one,card_two):
    '''Determine if one of the first two cards is an ace.
    
    :param card_one, card_two: strings -> cards dealt.
    :return: integer representing the sum of the two cards.

    '''
    ace_in_pair = False
    current_points = value_of_card(card_one) + value_of_card(card_two)
    
    if(value_of_card(card_one) == 1 or value_of_card(card_two) == 1 ):
        ace_in_pair = True

    if(ace_in_pair == True and current_points +10 <=21):
        current_points += 10
    
    return current_points

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    current_points = ace_in_first_hand(card_one,card_two)

    if(current_points + 11 <=21):
        ace = 11
    else:
        ace = 1
    
    return ace

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    current_points = ace_in_first_hand(card_one, card_two)
    if(current_points == 21):
        return True
    else:
        return False

def check_final_score(current_score):
    """Checks the score and sends appropriate message.
    param: current_score -> represents either two cards first dealt or two cards plus a third one.
    """
    if(current_score >21):
        print("Sorry. You've gone bust.")
    elif(current_score < 21):
        print("You're score is {}".format(current_score))
    else:
        print("Blackjack! Congrats.")
    
    return play_again()

    
def play_again():
    """After score is calculated and displayed the user chooses to play again or not.
    param: none
    retur: either invokes play_game() or sends a thank you message.
    """
    action = False
    play_again = input("Play again? yes/no. ")
    if(play_again == "yes"):
        action = play_game()
    elif(play_again == "no"):
        action = "Thanks for playing."
  
    return action



## GAME INSTANCES:------------------------------------------------------------------------------------------------------------
def play_game():
    print("Here are your cards.")
    card_one = deal_card()
    card_two = deal_card()
    print(card_one, card_two)
    if(is_blackjack(card_one,card_two)):
        print("Blackjack!")
        return play_again()
    else:
        ##ace_in_first_hand checks for an ace T/F it will return the score of the tow cards
        current_score = ace_in_first_hand(card_one,card_two)

        ##no black jack at this point so player can choose if they want to risk a third card or not.
        deal_third_card = input("Would you like another card?")
        if(deal_third_card =="yes"):
            card_three = value_of_card(deal_card())
            print(card_three)
            current_score +=card_three
            return check_final_score(current_score)
        else:
            return check_final_score(current_score)
    

print(play_game())


"""
BUG: If first ACE is calucalted as 11 but then third card is dealt going over 21 Ace should count as 1 again.
"""