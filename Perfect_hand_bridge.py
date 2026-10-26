# Fifty Challenging Problems in Probability by Frederick Mosteller

# Question08
# We often read of someone who has been dealt 13 spades at bridge. 
# With a well-shuffled pack of cards, 
# what is the chance that you are dealt a perfect hand (13 of one suit)? 
# (Bridge is played with an ordinary pack of 52 cards, 
# 13 in each of 4 suits, and each of 4 players is dealt 13.) 

from math import comb

card = comb(52, 13)
perfect = 4 # spades, hearts, diamonds, clubs

probability = perfect/card
print("Chance that you are dealt a perfect hand: ", probability*100, "%") 
# Chance that you are dealt a perfect hand: 6.29908e-10 %