import random

CARD_ENUM = {
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  '10': 10,
  'J': 10,
  'Q': 10,
  'K': 10,
  'A': 1,
}

suits = ['hearts', 'spades', 'clubs', 'diamonds']

# Shuffles indicate the number of shuffles that will be made
def permute_random(arr, shuffles):
  if (shuffles == 0): return arr
  random1 = random.randint(0, len(arr) - 1)
  random2 = random.randint(0, len(arr) - 1)
  arr[random1], arr[random2] = arr[random2], arr[random1]
  return permute_random(arr, shuffles - 1)