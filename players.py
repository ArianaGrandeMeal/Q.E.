import random
from components import ScoreCard, BidTile, IndustryToken

class Player:
    def __init__(self, 
            player_name, 
            player_number, 
            country, 
            industry, 
            tiles_won, 
            total_spent, 
            bid_amount,
            score_card, 
            bid_tile):
        
        self._player_name = player_name
        self._player_number = player_number
        self._country = country
        self._industry = industry
        self._tiles_won = tiles_won
        self._total_spent = total_spent
        self._bid_amount = bid_amount
        self._score_card = score_card
        self._bid_tile = bid_tile

class PlayerList():
    def __init__(self, _num_players):
        self._num_players = _num_players
        self._players = self._initialize_players(self._num_players)
        
    
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
        
        if num_players < 3:
            self.countries = self.countries[:3]        
            self.industries = self.industries[:3]
    
        for i in range(self.num_players):
            p = self._create_player(i)
            p_list.append(Player(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))
        return p_list

            
    def _create_player(self, i):
        self.player_number = i+1
        self.player_name = input(f"Player {self.player_number}, please enter your name:  ")
        self.tiles_won = []
        self.total_spent = 0
        self.bid_amount = 0
        self.country = self.countries.pop(random.randint(0, len(self.countries) - 1))
        self.industry = self.industries.pop(random.randint(0, len(self.industries) - 1))
        self.score_card = ScoreCard(self.player_name, self.country)
        self.bid_tile = BidTile(self.country)
        input("Please pass controller to next player, then press 'enter' key.\n")
        return [
            self.player_name, 
            self.player_number, 
            self.country, 
            self.industry, 
            self.tiles_won,
            self.total_spent,
            self.bid_amount,
            self.score_card,
            self.bid_tile
            ]

    
   
    
