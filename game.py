from components import Deck
from players import PlayerList
    
class Game():
    def __init__(self, num_players):
        self._players = PlayerList(num_players)
        self._deck = Deck(num_players)
        self._num_rounds = 16
        if num_players > 5:
            self.num_rounds = 15
            