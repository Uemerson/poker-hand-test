from PokerHand import PokerHand
from Result import Result

if __name__ == '__main__':
  poker_hand_1 = PokerHand("KS 2H 5C JD TD")
  poker_hand_2 = PokerHand("9C 9H 5C 5H AC")
  result = poker_hand_1.compare_with(poker_hand_2)
  print(result)
