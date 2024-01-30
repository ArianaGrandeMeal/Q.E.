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
        self._tied_bids = 0

        self._reveal_new_company_tile()
        self._get_open_bid()
        for player in self._other_players:
            self._get_private_bid(player)
        self._determine_winning_bid()
        

    def _reveal_new_company_tile(self):
        print(f"Round {self._round_number}.  The company tile up for auction is:\n",
              f"Country: {self._current_tile[0]}\n",
              f"Industry: {self._current_tile[1]}\n",
              f"Worth {self._current_tile[2]} victory points.\n")
        
    def _get_open_bid(self):
        print(f"{self._auctioneer}, you are the autioneer for this round.\n")
        self._opening_bid = int(input("Please enter your opening bid of at least $1 for the current tile."))
        # verify valid bid amount
        while self._opening_bid < 1 and isinstance(self._opening_bid, int):
            self._opening_bid = int(input("Invalid input.  Please enter your opening bid of at least $1: "))
        self._bids[self._auctioneer] = self._opening_bid
        
    def _get_private_bid(self, active_player):
            print(f"{active_player}, please enter your bid.  ")
            if active_player in self._zero_bids:
                bid = int(input("You may not bid zero this round. Please bid a whole number greater than zero"))
                while bid < 1 and isinstance(bid, int):
                    bid = int(input("Invalid bid. Please bid a whole number greater than zero. "))
            else:
                bid = int(input("You may place a bid of zero this round. Otherwise, your bid must be a whole number."))
                while bid < 0:
                    bid = int(input("Invalid bid. Please bid a whole number greater than or equal to zero. "))
            self._bids[active_player] = bid
    
    # finds max bid, evalutes for tied bids.  
    # If tied, calls _get_private_bid on tied players, then calls self to re-evaluate bids.
    # If three tied bids occur in a row, tied bids are eliminated and next highest bid wins.
    def _determine_winning_bid(self):
        # Determine highest bid, regardless of tie.
        max_bid = max(self._bids.values())
        
        # Check for tied max bids
        found = 0
        tied_bidders = []
        for bidder, bid in self._bids:
            if bid == max_bid:
                found += 1
                winning_bid = [bidder, bid]
                tied_bidders.append(bidder)
        # If tied, increment tied bid counter.
        if found > 1:
            self._tied_bids += 1
        
        # Check for 3 tied bids in a row.
        # If true, eliminate tied bids and determine highest remaining bid. 
            if self._tied_bids == 3:
                print("There are three tied bids in a row.\n",
                      "The tied bids are eliminated and the highest remaining bid wins.")
                for bidder in tied_bidders:
                    del self._bids[bidder]
                self._determine_winning_bid()
        
        # Otherwise, announce tied bid,vremove tied bids from bid dictionary, get new bids and evaluate.
            print("The following players tied for the max bid and must bid again.\n",
                  "Your bid may be more than, less than, or equal to your previous bet.\n",
                  "If there are three tied bids in a row, the highest non-tied bid wins the auction.")
            for bidder in tied_bidders:
                del self._bids[bidder]
                self._get_private_bid(bidder)
                self._determine_winning_bid()
        
        # If no tied bids, return winning bid
        return winning_bid
        
    
    def _award_tile(self, winning_bid):
        print("If you are not the auctioneer, please pass the controller to the auctioneer and turn away from the screen.")
        input(f"If you are the auctioneer, please press 'enter' to reveal winning bid.")
        print(f"{self._auctioneer}, the player who won the bid is {winning_bid[0]} with an amount of {winning_bid[1]}.\n",
              "Please announce the winning bidder's name--but not the bid amount--to the other players.")

       
        
