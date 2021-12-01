# Created by Charles R. Mousseau
# 2021 March 01

import constants

from random import uniform
from math import floor

class General:
	@staticmethod
	def cardVectorToString(cardList):
		output = ""

		for iter in range(len(cardList)):
			output += constants.CardStrings[cardList[iter]]
			if iter < len(cardList) - 1:
				output += " "
			
		return output
		
	@staticmethod
	def rollFromWeightedDist(weights):
		sumOfWeights = sum(weights)
		roll = int(floor(uniform(0, sumOfWeights)))

		for position in range(len(weights)):
			if roll < weights[position]:
				return position
			else:
				roll -= weights[position]
		
		raise Exception("rollFromWeightedDist(:) fell through weight array.")

	@staticmethod
	def weightedAverage(weights):
		sumOfResults = 0
		for index in range(len(weights)):
			sumOfResults += (weights[index] * index)
			
		return sumOfResults / float(sum(weights))