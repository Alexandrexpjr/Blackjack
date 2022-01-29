from helpers import CARD_ENUM

class Card:
  def __init__(self, card, suit):
    self.card = card
    self.suit = suit
    self.value = CARD_ENUM[str(self.card)]
    self.name = f'{card} of {suit}'

