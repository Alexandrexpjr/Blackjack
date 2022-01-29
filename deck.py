from helpers import permute_random

class Deck:
  def __init__(self):
    self.cardsObj = []
  
  def add_card(self, card):
    self.cardsObj.append(card)

  def shuffle(self, n):
    newOrder = permute_random(self.cardsObj, n)
    self.cardsObj = newOrder

  def drawCard(self):
    drawnCard = self.cardsObj.pop()
    return drawnCard

  def resetDeck(self):
    self.cardsObj = list(self.fullDeck)
  
  fullDeck = []

  






