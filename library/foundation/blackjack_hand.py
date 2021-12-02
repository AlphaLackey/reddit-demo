# Created by Charles R. Mousseau
# 2021 March 01

# import sys
# sys.path.append("library")

# from games.blackjack import Blackjack
# from hand import Hand

from hand import Hand
from library.games.blackjack import Blackjack

class BlackjackHand(Hand):
	def __init__(self):
		Hand.__init__(self)
		self.handTotal = 0
		self.isSoft = False

	def __str__(self):
		output = Hand.__str__(self)
		output += " = "
		output += "Soft " if self.isSoft else "Hard "
		output += self.handTotal.__str__()
		return output

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

	def blackjackRankAt(self, position):
		return Blackjack.cardNumberToBlackjackRank(self.cards[position])

	def clear(self):
		Hand.clear(self)
		self.isSoft = False
		self.handTotal = 0

	def drawCardFrom(self, sourceShoe):
		self.addCard(sourceShoe.drawCard())

	def isNatural(self): return self.handTotal == 21 and len(self.cards) == 2