from components import Deck
from players import PlayerList, AuctioneerList
from round import Round

class Game():
    def __init__(self, num_players):
        self._num_players = num_players
        self.deck = Deck(num_players)
        self._num_rounds = len(self.deck.tiles)
        self._player_list = PlayerList(num_players)
        self._player_names = [player[0] for player in self._player_list._players]
        self._auctioneer_list = AuctioneerList(self._player_names, self._num_rounds)
        self._round_num = 1
        self._cycles = 0
        self._full_cycle = False
        self._zero_bids = []
        self._auctioneer = None
        self._player_scores = []
        self._winning_bid = None
        
        
        self._new_game()
        
    
    
    def _new_game(self):
        # - call _new_round for the appropriate number of rounds
        # - set _full_cycle to True if each player has had a turn being the auctioneer to 
        #     signify that any players who have previously placed a zero bid may do so again
        # - reset _full_cycle to False after calling _new_round
        while self._round_num <= self._num_rounds:
            self._winning_bid = self._new_round(self._round_num, self._full_cycle)
            self._round_num += 1
            self._full_cycle = False
            if (self._round_num // self._num_players) > self._cycles:
                self._cycles += 1
                self._full_cycle = True
                self._zero_bids.clear() 
        
        # call _calculate_player_score for each player and add to list
        for player in self._player_list:
            self._player_scores.append(self._calculate_player_score(player, self._num_players))

    def _new_round(self, round_num, full_cycle):
        self._round_num = round_num
        self._full_cycle = full_cycle
        # clear the _other_players list.  maintains bid order when new auctioneer is assigned.
        
        # set next tile
        self._new_tile = self.deck.tiles.pop(self.deck.tiles[0])
        
        # set new auctioneer
        
        # create new round instance with updated variables
        self._current_round = Round(self._round_num,
                                    self._full_cycle,
                                    self._zero_bids, 
                                    self._auctioneer, 
                                    self._other_players, 
                                    self._new_tile)

    def _calculate_player_score(self, player, num_players):
        pass

    def _determine_winner(self, player_scores):
        pass


            