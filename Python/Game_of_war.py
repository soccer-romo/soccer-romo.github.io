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

import Card_module
import math

class War_Card(Card_module.Card):
	"""A War Card, Aces High"""
	@property
	def value(self):
		if self.is_face_up:
			if self.ranks == "J":
				v = 11
			elif self.ranks == "Q":
				v = 12
			elif self.ranks == "K":
				v = 13
			elif self.ranks == "A":
				v = 14
			else:
				v = War_Card.RANKS.index(self.ranks) + 1
		else:
			v = None
		return v

class War_Deck(Card_module.Deck):
	"""A War Deck"""
	def populate(self):
			for suit in War_Card.SUITS:
				for rank in War_Card.RANKS:
					self.add(War_Card(rank,suit))

def create_players(numbersOfPlayers = 2):
	players = []
	for person in range(numbersOfPlayers):
#		players.append("Players" + str(person))
		player = Card_module.Hand()
		players.append(player)
	return players


deck = War_Deck()
#print (deck)
deck.populate()
#print(deck)
deck.shuffle()
#print(deck)

players = create_players()
#print(players)
cardsPerPlayer = math.trunc(52 / len(players))
deck.deal(players, per_hand = cardsPerPlayer)

for player in players:
	for card in player.cards:
		print("Player", players.index(player))
		print(card.value)









"""
card1 = War_Card("A", "s")
print(card1)
print(card1.value)



card2 = War_Card("3", "c")
print(card2)
print(card2.value)

	
def build_deck():
	deck = {}
	suites = ["Hearts","Clubs","Spades","Diamonds"]
	for suite in suites:
		for n in range(13):
			deck[suite + str(n+1)] = n+1
	return deck
def deal(deck, players):
	
	

players = create_players()
print(players)
deck = build_deck()
print(deck)
"""
