import Deck, Player, Hand, Card

def main():
    # Make test player
    Player1 = Player.Player("Player1", Hand.Hand(), 10.0)

    # Make a rogue ace (testing ace being 11 or 1 functionality)
    rogueAce = Card.Card("SPADES", "ACE")

    # Make a deck, give it the default 52 cards, then shuffle it
    casinoDeck = Deck.Deck()
    casinoDeck.makeDefaultDeck()
    casinoDeck.shuffle()

    # Deal Player1's hand of 3 cards
    Player1.addCardToHand(casinoDeck.dealCard())
    Player1.addCardToHand(casinoDeck.dealCard())
    #Player1.addCardToHand(casinoDeck.dealCard())

    # Print Player1
    print(Player1.toString())

    # Add the rogue ace to Player1's hand twice
    Player1.addCardToHand(rogueAce)
    Player1.addCardToHand(rogueAce)

    # Print Player1 again to see how the hand value changed when given 2 aces
    print("\n\n", Player1.toString())

if __name__ == "__main__":
    main()

   