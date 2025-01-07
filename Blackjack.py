from src.Deck import *
from src.Player import *
from src.Card import *
from src.DealerAI import *
import src.HouseRules as RULES
import time
import os

def main():
    Player1 = Player("Matt", [], 0, False)
    Dealer = Player("Dealer", [], 0, False)


    casinoDeck = Deck(RULES.NUM_DECKS_IN_SHOE)
    casinoDeck.shuffle()

    Player1.addCardToHand(casinoDeck.dealCard())
    Player1.addCardToHand(casinoDeck.dealCard())

    Dealer.addCardToHand(casinoDeck.dealCard())
    Dealer.addCardToHand(casinoDeck.dealCard())
    

    while Player1.holdingBustedHand() == False and Player1.isStanding() == False:
        displayStatus(Player1)
        print("\n")
        displayDealerStatus(Dealer)
        print("What will you do?")
        print("1: Stand")
        print("2: Hit")
        action = input()
        
        if action == "2":
            Player1.addCardToHand(casinoDeck.dealCard())
            if Player1.holdingBustedHand() == True:
                print("Busted!!!")

        elif action == "1":
            Player1.becomesStanding()

    os.system('cls')

    print("\nExited player loop...")
    displayStatusBrief(Player1)
    print("\n\n")

    ### dealer's turn
    print("\n\nDealer's turn...")
    
    
    

    dealerIsDone = False

    DealersAI = DealerAI(Dealer)
    displayDealerStatusUnhiddenHand(Dealer)

    while dealerIsDone == False:

        action = DealersAI.getTurnDecision()
        print("The dealer decides to: ", action)

        if action == "HIT":
            Dealer.addCardToHand(casinoDeck.dealCard())
            if Dealer.holdingBustedHand() == True:
                dealerIsDone = True
        elif action == "STAND":
            dealerIsDone = True
        else:
            print("ERROR")

        #time.sleep(2)
        #displayDealerStatusUnhiddenHand(Dealer)

        displayDealerStatusUnhiddenHand(Dealer)

    ## make decision

    print("\n\nDECISION: ")

    #player busted dealer busted

    if Player1.holdingBustedHand() == True and Dealer.holdingBustedHand()  == True:
        print("Both you and the dealer busted. You lost your bet...")

    #player bust dealer not bust
    elif Player1.holdingBustedHand()  == True and Dealer.holdingBustedHand()  == False:
        print("You busted and the dealer didn't. You lost your bet...")

    # player bust dealer not bust
    elif Player1.holdingBustedHand()  == False and Dealer.holdingBustedHand()  == True:
        print("You did not bust and the dealer did. You doubled your bet...")


    #player not bust dealer not bust
    elif Player1.holdingBustedHand()  == False and Dealer.holdingBustedHand()  == False:
        # check which hand is higher
        if Player1.getHandValue() == Dealer.getHandValue():
            print("You and the dealer had the same hand value. You get your bet back...")
        elif Player1.getHandValue() > Dealer.getHandValue():
            print("You had a better hand than the dealer. You doubled your bet...")
        elif Player1.getHandValue() < Dealer.getHandValue():
            print("The dealer had a better hand than you. You lost your bet...")
        else:
            print("Error..")
    else:
        print("Error 2..")
    

def displayStatus(player: Player) -> None:
    print("Current hand: ", player.getHand())
    print("Value: ", str(player.getHandValue()))
    #print("Soft: ", str(player.handIsSoft()))
    #print("Splittable: ", str(player.handIsSplittable()))
    return

def displayStatusBrief(player) -> None:
    print("Final hand: ", player.getHand())
    print("Final Value: ", player.getHandValue())

def displayDealerStatus(dealer) -> None:
    print("Dealer showing: [", dealer.getFirstPositionCard().toString(), "]")
    return

def displayDealerStatusUnhiddenHand(dealer) -> None:
    print("Dealer hand: [", dealer.getHand(), "]")
    print("Value: ", dealer.getHandValue())
    return

if __name__ == "__main__":
    main()