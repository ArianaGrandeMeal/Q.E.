import random

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
        self.tiles = self._create_company_tile_deck(self.num_players)

    
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

class IndustryToken():
    def __init__(self, industry):
        self._industry = industry
        
