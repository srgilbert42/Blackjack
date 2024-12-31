from typing import List
import Deck
import Player
import Hand
import Card

class Blackjack:
    #players, deck, dealer

    def __init__(self, players: List, deck: Deck):
        self.players = players
        self.deck = deck