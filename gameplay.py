class Round():
    def __init__(self, players):
        self.players = players
        self._num_rounds = 16
        if len(self.players) > 4:
              self._num_rounds = 15
              
    # need to finish later
    def _select_new_auctioneer(self, round_number):
        _round_index = self._num_rounds % round_number
        _auctioneer = self.players[_round_index]

# drawn_tile = draw_company_tile(company_tile_deck)   <--- to be completed