class Round:
    def __init__(self, round_number, zero_bid_cycle, zero_bids, auctioneer, other_players, round_tile):
        self._round_number = round_number
        self._zero_bid_cycle = zero_bid_cycle
        self._zero_bids = zero_bids
        self._auctioneer = auctioneer
        self._other_players = other_players
        self._current_tile = round_tile
        self._opening_bid = None
        self._bids = dict()

        self._reveal_new_company_tile()
        self._get_open_bid()
        for player in self._other_players:
            self._get_private_bid(player)

    def _reveal_new_company_tile(self):
        print(f"Round {self._round_number}.  The company tile up for auction is:\n")
        print(f"Country: {self._current_tile[0]}") 
        print(f"Industry: {self._current_tile[1]}")
        print(f"Worth {self._current_tile[3]} victory points.\n")
        
    def _get_open_bid(self):
        print(f"{self._auctioneer}, you are the autioneer for this round.\n")
        self._opening_bid = int(input("Please enter your opening bid of at least $1 for the current tile."))
        while self._opening_bid < 1:
            self._opening_bid = int(input("Invalid input.  Please enter your opening bid of at least $1: "))
        self._bids[self._auctioneer] = self._opening_bid
        
    def _get_private_bid(self, active_player):
            print(f"{active_player}, please enter your bid.  ")
            if active_player in self._zero_bids:
                bid = int(input("You may not bid zero this round. "))
                while bid < 1:
                    bid = int(input("Invalid bid. Please enter a bid greater than zero. "))
            else:
                bid = int(input("You may place a bid of zero this round. "))
                while bid < 1:
                    bid = int(input("Invalid bid. Please enter a bid greater than or equal to zero. "))
            self._bids[active_player] = bid
    
    def _check_for_tied_bids(self):
        found = 0
        tied_bids = []
        max_bid = max(self._bids.values())
        for bid in self._bids.values():
            if bid == max_bid:
                found += 1
                tied_bids.append([max_bid])
        if found < 1:


    
    def _determine_winning_bid(self):
        
        max_bid = max(self._bids.values())
        bidder = {i for i in self._bids if self._bids[i] == max_bid}
        winning_bid = [max_bid, bidder]
        
        # check for tied max bids
        found = 0
        tied_bidders = []
        for bid in self._bids.values():
            if bid == max_bid:
                found += 1
                tied_bidders.append(winning_bid)
        if found < 1:
            
        

        
        return winning_bid

        
        


            
                
                    
                
                
                


        