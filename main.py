from game import Game
'''
###############################################################################
# Virtual edition of QE (Quantitative Easing) board game
# Code by Tripp Sellers
# Created 10/31/2023
# 
# Credits for print version:
#   Game designer: Gavin Birnbaum
#   Artist: Anca Gavril
#   Rules Editing: Travis D. Hill
#   CG Artist: Filip Gavril
# 
# Publisher information: 
#   Published 2020
#   BoardGameTables.com
#   www.boardgametables.com
#   17501 W 98th St, BLDG 5219
#   Lenexa, KS 66219 US
#   games@boardgametables.com
#   +1 913-602-8878
###############################################################################
'''

def main():

    input("Welcome to Q.E.  Press 'enter' to begin.")
        
    # get number of players
    _num_players = input("Please enter the number of players.")
    while 5 < _num_players < 3:
        print("Invalid player count.  Number of players must be between 3 and 5.\n")
        _num_players = input("Please enter the number of players.")
    
    
    game = Game(_num_players)
    
    
main()
