#black jack game

import Card_module

#Card_module.sayHello()

card1 = Card_module.Card("a","s",True)

#print(card1)

card2 = Card_module.Card("2", "s", True)

#print(card2)

deck1 = Card_module.Deck()
deck1.populate()
#print(deck1)
deck1.shuffle()
print(deck1)
player_hand1 = Card_module.Hand()
player_hand2 = Card_module.Hand()

deck1.deal([player_hand1,player_hand2], 5)

print(player_hand1)