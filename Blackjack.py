from src.Deck import *
from src.Player import *
from src.Card import *
import src.HouseRules as RULES

def main():
    Player1 = Player("Matt", [], 0, False)
    Dealer = Player("Dealer", [], 0, False)


    casinoDeck = Deck(RULES.NUM_DECKS_IN_SHOE)
    casinoDeck.shuffle()

    Player1.addCardToHand(casinoDeck.dealCard())
    Player1.addCardToHand(casinoDeck.dealCard())

    Dealer.addCardToHand(casinoDeck.dealCard())
    Dealer.addCardToHand(casinoDeck.dealCard())
    

    while not Player1.holdingBustedHand():
        displayStatus(Player1)
        print("\n\n")
        displayDealerStatus(Dealer)
        print("What will you do?")
        print("1: Stand")
        print("2: Hit")
        action = input()
        
        if action == "2":
            Player1.addCardToHand(casinoDeck.dealCard())
        elif action == "1":
            break


def displayStatus(player: Player) -> None:
    print("Current hand: ", player.getHand())
    print("Value: ", str(player.getHandValue()))
    print("Soft: ", str(player.handIsSoft()))
    print("Splittable: ", str(player.handIsSplittable()))
    return

def displayDealerStatus(dealer) -> None:
    print("Dealer showing: [", dealer.getFirstPositionCard().toString(), "]")
    return






if __name__ == "__main__":
    main()