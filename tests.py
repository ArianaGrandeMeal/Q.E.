import random

def main():

    input("Welcome to Q.E.  Press 'enter' to begin.\n")
        
    # get number of players
    _num_players = int(input("Please enter the number of players:  "))
    while not (3 <= _num_players <= 5):
        print("Invalid player count. Number of players must be between 3 and 5.\n")
        _num_players = int(input("Please enter the number of players: "))

    deck = Deck(_num_players)
    players = PlayerList(_num_players)
    

    for player in players._players:
        for attr in dir(player):
            print(f"{attr}: {getattr(player, attr)}")
        print()


class Deck():
    def __init__(self, num_players):
       
        # Company tile deck will be generated from this list.
        self.BASE_COMPANY_TILES = [
            {'Country': 'China', 'Industry': 'Manufacturing', 'Points': 1, 'remove': [5]},
            {'Country': 'China', 'Industry': 'Agriculture', 'Points': 2, 'remove': [0]},
            {'Country': 'China', 'Industry': 'Housing', 'Points': 3, 'remove': [0]},
            {'Country': 'China', 'Industry': 'Finance', 'Points': 4, 'remove': [5]},
            {'Country': 'China', 'Industry': 'Government', 'Points': 4, 'remove': [3,4]},    
            {'Country': 'Japan', 'Industry': 'Manufacturing', 'Points': 2, 'remove': [0]},
            {'Country': 'Japan', 'Industry': 'Agriculture', 'Points': 3, 'remove': [5]},
            {'Country': 'Japan', 'Industry': 'Housing', 'Points': 4, 'remove': [0]},
            {'Country': 'Japan', 'Industry': 'Finance', 'Points': 1, 'remove': [5]},
            {'Country': 'Japan', 'Industry': 'Government', 'Points': 3, 'remove': [3,4]},    
            {'Country': 'U.S.', 'Industry': 'Manufacturing', 'Points': 3, 'remove': [0]},
            {'Country': 'U.S.', 'Industry': 'Agriculture', 'Points': 4, 'remove': [0]},
            {'Country': 'U.S.', 'Industry': 'Housing', 'Points': 1, 'remove': [5]},
            {'Country': 'U.S.', 'Industry': 'Finance', 'Points': 2, 'remove': [0]},    
            {'Country': 'E.U.', 'Industry': 'Manufacturing', 'Points': 4, 'remove': [0]},
            {'Country': 'E.U.', 'Industry': 'Agriculture', 'Points': 1, 'remove': [5]},
            {'Country': 'E.U.', 'Industry': 'Housing', 'Points': 2, 'remove': [0]},
            {'Country': 'E.U.', 'Industry': 'Finance', 'Points': 3, 'remove': [0]},    
            {'Country': 'U.K.', 'Industry': 'Agriculture', 'Points': 3, 'remove': [3,4]},
            {'Country': 'U.K.', 'Industry': 'Finance', 'Points': 4, 'remove': [3,4]},
            {'Country': 'U.K.', 'Industry': 'Government', 'Points': 2, 'remove': [3,4]},
            ]
        
        self.num_players = num_players
        self.shuffled = self._create_company_tile_deck(self.num_players)

    
    def _create_company_tile_deck(self, num_players):
        
        # iterative comprehension of base company tile list to remove unused tiles.
        # copies base list, skipping tile if num_players is found in the tile's 'remove' value
        self.initialized_deck = [self.BASE_COMPANY_TILES[i] for i in range(len(self.BASE_COMPANY_TILES)) if num_players not in self.BASE_COMPANY_TILES[i]['remove']]
        
        # shuffle and return deck 
        random.shuffle(self.initialized_deck)
        return self.initialized_deck
    
class ScoreCard():
    def __init__(self, player_name, country):
        self._player_name = player_name
        self._country = country
        self._company_vp = 0
        self._zero_bids = 0
        self._nationalization = 0
        self._industries = dict(Financial = 0, Agriculture = 0, Housing = 0, Manufacturing = 0, Government = 0)
        
class BidTile():
    def __init__(self, country):
        self._country = country
        self._bid_amount = 0

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
            


main()

