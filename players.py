import random
from itertools import cycle


class Player:
    def __init__(self, 
            player_name, 
            player_country, 
            player_industry,
            bid_amount,
            zero_bids,
            tile_vp,
            tile_countries,
            tile_industries,
            total_spent 
            ):
        
        self._player_name = player_name
        self._player_country = player_country
        self._player_industry = player_industry
        self.bid_amount = bid_amount
        self.zero_bids = zero_bids
        self.tile_vp = tile_vp
        self.tile_countries = tile_countries
        self.tile_industries = tile_industries
        self.total_spent = total_spent
        
        
        

class PlayerList():
    def __init__(self, _num_players):
        self._num_players = _num_players
        self._players = self._initialize_players(self._num_players)
        self._auctioneer_list = self._initialize_auctioneer_list(self._players)

    def _create_player(self):
        self.player_name = input(f"Player {self.player_number}, please enter your name:  ")
        self.player_country = self.countries.pop(random.randint(0, len(self.countries) - 1))
        self.player_industry = self.industries.pop(random.randint(0, len(self.industries) - 1))
        self.bid_amount = 0
        self.zero_bids = 0
        self.tile_vp = 0
        self.tile_countries = []
        self.tile_industries = []
        self.total_spent = 0
        input("Please pass controller to next player, then press 'enter' key.\n")
        return [
            self.player_name, 
            self.player_country, 
            self.player_industry,
            self.bid_amount,
            self.zero_bids,
            self.tile_vp,
            self.tile_countries,
            self.tile_industries,
            self.total_spent]

        
    
    '''
    # initialize player list as list of Player objects.  if statement ensures 
    # players aren't assigned a country or industry that is not in the game if 
    # less than 5 players.  Each object initializes to player number, random 
    # country and industry, an empty list for tiles_won, and 0 for total spent.
    '''
    def _initialize_players(self, num_players):
        COUNTRIES = ['China', 'Japan', 'U.S.', 'E.U.', 'U.K.']
        INDUSTRIES = ['Manufacturing', 'Agriculture', 'Housing', 'Finance', 'Government']
        
        self.num_players = num_players
        self.countries = COUNTRIES
        self.industries = INDUSTRIES
        p_list = []
        
        if num_players < 5:
            self.countries = self.countries[:3]        
            self.industries = self.industries[:3]
    
        i = 1
        while i <= self.num_players:
            p = self._create_player()
            p_list.append(Player(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))
            i+=1
        return p_list

    def _initialize_auctioneer_list(self, p_list):
        self.p_list = p_list
        auctioneer_list = []
        p_list_cycle = cycle(self.p_list)

        num_rounds = 16
        if len(self.p_list) == 5:
            num_rounds = 15

        round = 1
        while round <= num_rounds:
            auctioneer_list.append(next(p_list_cycle[0]))
            round += 1
        return auctioneer_list
    
    
    