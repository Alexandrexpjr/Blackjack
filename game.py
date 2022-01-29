from deck import Deck
from card import Card
from helpers import CARD_ENUM, suits
from player import Player

class Game:
  def __init__(self, deck, players):
    self.players = players
    self.deck = deck
    self.players_info = {}
    for player in players:
      self.players_info[player.name] = 0

  def check_winner(self):
    values = []
    winners = []
    for value in self.players_info.values():
      if(value <= 21): # if the player doesn't bust
        values.append(value) # All values are in the list
    max_value = 0
    if (len(values) > 0): max_value = max(values)
    for player in self.players_info:
      if self.players_info[player] == max_value: winners.append(player)

    if (len(winners) == 0): return print('Nobody wins :(')
    if (len(winners) == 1): return print(f'{winners[0]} won the game!')
    if (len(winners) > 1): return print(f'{", ".join(winners)} tied with {max_value} and won the game!')

  def reset_game(self):
    self.deck.resetDeck()
    for player in self.players:
      player.reset_cards()

  def check_sum(self, player):
    sum = 0
    for value in player.get_cards_value():
      sum += value

    has_ace = player.checkAce()

    if (sum <= 11 and has_ace): sum += 10 # Here, if the player has an ace and the sum is lower or equal than 11, Ace assume the value of 11
    self.players_info[player.name] = sum

    return sum

  def sum_handler(self, player):
    sum = self.check_sum(player)
    if (sum < 21): print(f'{player.name} has made {sum}.')
    if (sum == 21): print(f'Amazing! {player.name} has made {sum}!')
    if (sum > 21): print(f'Busted! {player.name} have a total over 21.')

  def check_stop(self, player):
    stop = False
    print(f"{player.name}'s turn.")
    print(player.get_cards_name())
    while (stop == False):
      wanna_stop = input('Do you want to stop? Y/N ')
      if(wanna_stop == 'N'):
        player.drawCard(self.deck.drawCard())
        print(player.get_cards_name())
        sum = self.check_sum(player)
        if sum >= 21: stop = True
      else: stop = True

  def start(self):
    self.deck.shuffle(50)
    for player in self.players:
      player.drawCard(self.deck.drawCard())
      player.drawCard(self.deck.drawCard())
      # Here, every player has 2 cards in hand

    for player in self.players:
      self.check_stop(player)
      self.sum_handler(player)

    self.check_winner()
    play_again = input('Do you want to play again? Y/N ')
  
    self.reset_game()

    if (play_again == 'Y'): self.start()
    else: print('Bye!')

# Setup the deck
deck = Deck()
for suit in suits:
  for key in CARD_ENUM:
    card = Card(key, suit)
    deck.add_card(card)

deck.fullDeck = deck.cardsObj.copy() # To have a reference of the fullDeck

player1 = Player('Isabella')
player2 = Player('Alexander')
player3 = Player('Julia')
player4 = Player('John')

game = Game(deck, [player1, player2, player3, player4])

game.start()

