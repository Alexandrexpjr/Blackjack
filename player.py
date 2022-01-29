class Player:
  def __init__(self, name):
    self.name = name
    self.cards = []

  def drawCard(self, card):
    self.cards.append(card)

  def get_cards_name(self):
    cards_name = []
    for card in self.cards:
      cards_name.append(card.name)
    return cards_name

  def get_cards_value(self):
    cards_name = []
    for card in self.cards:
      cards_name.append(card.value)
    return cards_name

  def reset_cards(self):
    self.cards = []

  def checkAce(self):
    for card in self.cards:
      if card.card == 'A': return True
    return False
      