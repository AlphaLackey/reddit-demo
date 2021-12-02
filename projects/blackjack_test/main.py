import sys
print("\nsys.path:")
print("-------")
print (sys.path)
print("")

import os
print("cwd:")
print("----")
print(os.getcwd())
print("")

from library.foundation.blackjack_hand import BlackjackHand
foo = BlackjackHand()

# hole_cards = [-1] * 2
# result_map = {}

# player_hand = BlackjackHand()

# for hole_cards[0] in range(52):
# 	for hole_cards[1] in range(hole_cards[0] + 1, 52):
		
# 		player_hand.clear()
# 		for card in hole_cards:
# 			player_hand.addCard(card)

# 		this_result = player_hand.handTotal

# 		if not this_result in result_map.keys():
# 			result_map[this_result] = 0

# 		result_map[this_result] += 1

# for data in result_map:
# 	print(data, result_map[data])
