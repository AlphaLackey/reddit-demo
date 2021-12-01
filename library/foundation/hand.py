# Created by Charles R. Mousseau
# 2021 March 01

import general

class Hand:
	def __init__(self):
		self.cards = []

	def __str__(self):
		return "[ " + general.General.cardVectorToString(self.cards) + " ]"
		
	def clear(self):
		self.cards = []

	def addCard(self, cardNumber):
		self.cards.append(cardNumber)