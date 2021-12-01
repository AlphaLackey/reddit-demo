# Created by Charles R. Mousseau
# 2021 March 01

from hand import Hand
from blackjack import Blackjack

class BlackjackHand(Hand):
    def __init__(self):
        Hand.__init__(self)
        self.handTotal = 0
        self.isSoft = False

    def addCard(self, cardNumber):
        Hand.addCard(self, cardNumber)
        blackjackRank = Blackjack.cardNumberToBlackjackRank(cardNumber)

        if blackjackRank == 1:
            if self.isSoft:
                self.handTotal += 1
            else:
                self.handTotal += 11
                self.isSoft = True
        else:
            self.handTotal += 10 if blackjackRank == 0 else blackjackRank

        if self.isSoft and self.handTotal > 21:
            self.isSoft = False
            self.handTotal -= 10

    def clear(self):
        Hand.clear(self)
        self.isSoft = False
        self.handTotal = 0
