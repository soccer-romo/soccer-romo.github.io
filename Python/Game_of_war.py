# each card a has a suite and number
#make sure there is only 4 of each Card
#each player is dealt cards at random
#highest cards wins
# tie breaker - 3 cards face down, 1 up, Winner takes all
#52 cards total
#winner is determined who gets all cards
# 2 players

#psudocode
# build and shuffle the deck (build_deck) , shuffle.build_deck
# create players:: player1,player2
# deal the cards
# play the games

def create_players(numbersOfPlayers = 2):
	players = []
	for person in range(numbersOfPlayers):
		players.append("Players" + str(person))
	return players
	
def build_deck():
	deck = {}
	suites = ["Hearts","Clubs","Spades","Diamonds"]
	for suite in suites:
		for n in range(13):
			deck[suite + str(n+1)] = n+1
	return deck
#def deal(deck, players):
		
	

players = create_players()
print(players)
deck = build_deck()
print(deck)

