import random

class Deck():
    def __init__(self, num_players):
        # Company tile deck will be generated from this list.
        BASE_COMPANY_TILES = [
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
        self.base_tiles = BASE_COMPANY_TILES
        self.deck = self._create_company_tile_deck(self.num_players)

    
    def _create_company_tile_deck(self, num_players):
        
        # iterative comprehension of base company tile list to remove unused tiles.
        # copies base list, skipping tile if num_players is found in the tile's 'remove' value
        initialized_deck = [self.base_tiles[i] for i in range(len(self.base_tiles)) if num_players not in self.base_tiles[i]['remove']]
        
        # shuffle and return deck 
        return self._shuffle_deck(initialized_deck)
    
    def _shuffle_deck(self, deck):
        _shuffled_deck = []
        while len(deck) > 0:
            _shuffled_deck.append(deck.pop(random.choice(deck)))
        return _shuffled_deck


class ScoreCard():
    pass

class BidTile():
    pass

class IndustryToken():
    pass
        
