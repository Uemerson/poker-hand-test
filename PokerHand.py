from Result import Result

cards_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

class PokerHand:
  def isDenominationSequence(self, hand):
    hand_values = [cards_values[hand[i][0]] for i in range(0,5)]
    return sorted(hand_values) == list(range(min(hand_values), max(hand_values)+1))

  def isSameDenomination(self, hand, denomination_compare):
    hand_values = [hand[i][0] for i in range(0,5)]

    repeat_denominations = []
    for value in set(hand_values):
      repeat_denominations.append(hand_values.count(value))

    return sorted(repeat_denominations) == denomination_compare

  def isSameSuit(self, hand, suit_compare):
    hand_suits = [hand[i][1] for i in range(0,5)]

    repeat_suits = []
    for suit in set(hand_suits):
      repeat_suits.append(hand_suits.count(suit))

    return sorted(repeat_suits) == suit_compare

  def checkRoyalFlush(self, hand):
    hand_values = [cards_values[hand[i][0]] for i in range(0,5)]
    return (sorted(hand_values) == list(range(10, 15))) & self.isSameSuit(hand, [5])

  def checkStraightFlush(self, hand):
    return self.isDenominationSequence(hand) & self.isSameSuit(hand, [5])

  def checkFourOfAKind(self, hand):
    return self.isSameDenomination(hand,  [1, 4])

  def checkFullHouse(self, hand):
    return self.isSameDenomination(hand, [2, 3])

  def checkTwoPair(self, hand):
    return self.isSameDenomination(hand, [1, 2, 2])

  def checkOnePair(self, hand):
    return self.isSameDenomination(hand, [1, 1, 1, 2])

  def checkFlush(self, hand):
    return self.isSameSuit(hand, [5])

  def checkStraight(self, hand):
    return self.isDenominationSequence(hand)

  def checkThreeOfAKind(self, hand):
    return self.isSameDenomination(hand, [1, 1, 3])

  def highCard(self, hand):
    cards_values_replace = cards_values.copy()
    cards_values_replace['A'] = 1                             # nesse caso o A se torna 1
    hand_values = [cards_values_replace[hand[i][0]] for i in range(0,5)]
    return sorted(hand_values, reverse=True)[0]

  def checkPokerHand(self, hand):
    if self.checkRoyalFlush(hand):
      print(f'is royal flush')
    elif self.checkStraightFlush(hand): 
      print(f'is straight flush')
    elif self.checkFourOfAKind(hand):
      print(f'is four of a kind')
    elif self.checkFullHouse(hand):
      print(f'is full house')
    elif self.checkFlush(hand):
      print(f'is flush')
    elif self.checkStraight(hand):
      print(f'is straight')
    elif self.checkThreeOfAKind(hand):
      print(f'is three of a kind')
    elif self.checkTwoPair(hand):
      print(f'is two par')
    elif self.checkOnePair(hand):
      print(f'is one par')
    else:
      print(f'high card is: {self.highCard(hand)}')

  def powerPokerHand(self, hand):
    if self.checkRoyalFlush(hand):
      return 10
    elif self.checkStraightFlush(hand): 
      return 9
    elif self.checkFourOfAKind(hand):
      return 8
    elif self.checkFullHouse(hand):
      return 7
    elif self.checkFlush(hand):
      return 6
    elif self.checkStraight(hand):
      return 5
    elif self.checkThreeOfAKind(hand):
      return 4
    elif self.checkTwoPair(hand):
      return 3
    elif self.checkOnePair(hand):
      return 2
    else:
      return 0

  def compare_with(self, anotherPokerHand):
    hand1 = self.powerPokerHand(self.cards) 
    hand2 = self.powerPokerHand(anotherPokerHand.cards) 

    if (hand1 == hand2):
      if self.highCard(self.cards) > self.highCard(anotherPokerHand.cards):
        return Result.WIN
      else:
        return Result.LOSS
    elif (hand1 < hand2):
      return Result.LOSS

    return Result.WIN
  
  def __init__(self, cards): 
      self.cards = cards.split(' ')