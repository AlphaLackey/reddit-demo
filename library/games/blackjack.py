# Created by Charles R. Mousseau
# 2021 March 01

import math

class Blackjack:
    @staticmethod
    def cardNumberToBlackjackRank(cardNumber):
        cardRank = int(math.floor(cardNumber / 4))
        if cardRank == 12:
            return 1
        elif cardRank >= 8:
            return 0
        else:
            return cardRank + 2

