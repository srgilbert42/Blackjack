from src.Deck import *
from src.Player import *
from src.Card import *
from src.DealerAI import *
from src.CustomException import *
from src.NotEnoughMoneyException import *
from src.AmountLowerThanMinimumException import *
import src.HouseRules as RULES
import time

# TODO
# implement splitting
# implement betting
# implement blackjack (ace + facecard)
# implement support for multiple players?
# implement player AI and automating player1
# implement doubling down
# initializing hands should be done after better stage
# make gameplay loop repeat, make sure to reset necessary variables
# make decks refresh themselves if the number of cards left is getting lower than some amount
# cleanup output screen (inconsistent newlines, tabbing, etc)

def main():
    # Init Player1, Dealer, the deck, and gameplay loop variables
    playerGameOver = False
    Player1 = Player("Matt", [], 100.0)
    Dealer = Player("Dealer", [], 0)
    casinoDeck = Deck(RULES.NUM_DECKS_IN_SHOE)
    casinoDeck.shuffle()

    # Begin gameplay loop

    while playerGameOver == False:

        # Check for gameover

        if Player1.getMoney() < 5.0:
            print("You have less money than the minimum amount needed to bet. Game over...,,")
            playerGameOver = True
            break

        # Reset states

        Player1.resetState()
        Dealer.resetState()


        # Get player bet
        print("BET STAGE")

        playerBetInputIsValid = False
        while playerBetInputIsValid == False:

            try:
                print("\tPlace your bet ( current balance:", Player1.getMoney(), ")")
                playerBet = float(input())
                if playerBet > Player1.getMoney():
                    raise NotEnoughMoneyException("\tYou cannot bet more money than you have... try reading....,,")
                if playerBet < 5.0:
                    raise AmountLowerThanMinimumException("\tYou MUST bet a minimum of 5.0 to play.")
            except ValueError:
                print("\tEnter only a floATING POINT NUMBER...!!!!..,,")
            except NotEnoughMoneyException as ex:
                print(ex.message)
            except AmountLowerThanMinimumException as ex:
                print(ex.message)
            else:
                playerBetInputIsValid = True

        # Subtract bet from player money and display new amount

        Player1.subtractMoney(playerBet)
        print("New money: ", Player1.getMoney())

        # Deal cards

        Player1.addCardToHand(casinoDeck.dealCard())
        Player1.addCardToHand(casinoDeck.dealCard())

        Dealer.addCardToHand(casinoDeck.dealCard())
        Dealer.addCardToHand(casinoDeck.dealCard())

        # Begin player turn

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

        # End player turn

        print("\nExited player loop...")
        displayStatusBrief(Player1)
        print("\n\n")

        # Dealer's turn

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

            displayDealerStatusUnhiddenHand(Dealer)

        # Make decision

        print("\n\nDECISION: ")

        # Player busted and dealer busted

        if Player1.holdingBustedHand() == True and Dealer.holdingBustedHand()  == True:
            print("Both you and the dealer busted. You lost your bet...")

        # Player bust dealer not bust
        elif Player1.holdingBustedHand()  == True and Dealer.holdingBustedHand()  == False:
            print("You busted and the dealer didn't. You lost your bet...")

        # Player not bust dealer bust
        elif Player1.holdingBustedHand()  == False and Dealer.holdingBustedHand()  == True:
            print("You did not bust and the dealer did. You doubled your bet...")
            Player1.addMoney(2.0 * playerBet)


        # Player not bust dealer not bust
        elif Player1.holdingBustedHand()  == False and Dealer.holdingBustedHand()  == False:

            # check which hand is higher

            if Player1.getHandValue() == Dealer.getHandValue():
                print("You and the dealer had the same hand value. You get your bet back...")
                Player1.addMoney(playerBet)

            elif Player1.getHandValue() > Dealer.getHandValue():
                print("You had a better hand than the dealer. You doubled your bet...")
                Player1.addMoney(2.0 * playerBet)

            elif Player1.getHandValue() < Dealer.getHandValue():
                print("The dealer had a better hand than you. You lost your bet...")
            else:
                print("Error..")
        else:
            print("Error 2..")

    print("End...,,")
    

def displayStatus(player: Player) -> None:
    print("Current hand: ", player.getHandBrief())
    print("Value: ", str(player.getHandValue()))
    #print("Soft: ", str(player.handIsSoft()))
    #print("Splittable: ", str(player.handIsSplittable()))

def displayStatusBrief(player) -> None:
    print("Final hand: ", player.getHandBrief())
    print("Final Value: ", player.getHandValue())

def displayDealerStatus(dealer) -> None:
    print("Dealer showing: [", dealer.getFirstPositionCard().toString(), "]")

def displayDealerStatusUnhiddenHand(dealer) -> None:
    print("Dealer hand: ", dealer.getHandBrief())
    print("Value: ", dealer.getHandValue())

if __name__ == "__main__":
    main()