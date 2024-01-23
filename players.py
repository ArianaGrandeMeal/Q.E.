import random

class Player:
    def __init__(self, 
            player_name, 
            player_number, 
            country, 
            industry, 
            tiles_won=None, 
            total_spent=None):
        
        self.player_name = player_name
        self.player_number = player_number
        self.country = country
        self.industry = industry
        self.tiles_won = tiles_won
        self.total_spent = total_spent

class PlayerList():
    def __init__(self, _num_players):
        self._num_players = _num_players
        self._players = []
        self._initialize_players(self._num_players)
    
    def _create_player(self, i):
        self.player_number = i+1
        self.player_name = input(f"Player {self.player_number}, please enter your name:  ")
        self.country = self.countries.pop(random.choice(self.countries))
        self.industry = self.industries.pop(random.choice(self.industries))
        self.tiles_won = []
        self.total_spent = 0
        return (
            self.player_name, 
            self.player_number, 
            self.country, 
            self.industry, self.tiles_won,
            self.total_spent 
            )

    
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
        
        if num_players < 5:
            self.countries = self.countries[:3]        
            self.industries = self.industries[:3]
    
        for i in range(self.num_players):
            self._players.append(Player(self._create_player(i)))
    
