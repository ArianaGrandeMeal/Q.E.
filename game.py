import random
from components import Deck
from players import PlayerList
from round import Round

class Game():
    def __init__(self, num_players):
        self._num_players = num_players
        self._players = PlayerList(num_players)
        self._deck = Deck(num_players)
        self._num_rounds = 16
        self._zero_bids = []
        self._auctioneer = None
        self._start_index = random.choice(self._players._player_number)
        
        if num_players == 5:
            self.num_rounds = 15
        
        for i in range(self._players):
            self._auctioneer_indexes.append(i+1)
        
        self._new_game(self._num_rounds)
        
    # call _new_round for the appropriate number of rounds
    # call _calculate_player_score for each player and add to list
    def _new_game(self, num_rounds):
        self._player_scores = []

        i = 1
        while i <= num_rounds:
            self._new_round(i)

        for player in self._players:
            self._player_scores.append(self._calculate_player_score(player, self._num_players))

    def _new_round(self, round_number):
        # set new auctioneer
        self._auctioneer_index = ((round_number + self._start_index) % self._num_players) + 1
        for player in self._players:
            if self._auctioneer_index == player._player_number:
                self._auctioneer = player._player_name
        
        self._current_round = Round(round_number, self._auctioneer)

    def _calculate_player_score(self, player, num_players):
        pass

    def _determine_winner(self, player_scores):
        pass


            