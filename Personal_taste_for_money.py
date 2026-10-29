# Fifty Challenging Problems in Probability by Frederick Mosteller

# Question10
# (a) An urn contains \0 black balls and \0 white balls, 
# identical except for color. 
# You choose "black" or "white." One ball is drawn at random,
# and if its color matches your choice, you get $\0, otherwise nothing. 
# Write down the maximum amount you are willing to pay to play the game. 
# The game will be played just once.
# (b) A friend of yours has available many black and many white balls,
# and he puts black and white balls into the urn to suit himself. 
# You choose "black" or "white." A ball is drawn randomly from this urn. 
# Write down the maximum amount you are willing to pay to play this game. 
# The game will be played just once. 

black = 10
white = 10
total = 20
win = 10
lose = 0

probability_white = white/total
print("Probability -> win if you choose white ball: ", probability_white*100, "%")
probability_black = black/total
print("Probability -> win if you choose black ball: ", probability_black*100, "%")
prob_lose = 1 - probability_white
print("Probability -> lose if you choose black or white balls: ", (1-probability_white)*100, "%")

# expected value - only use 1 -> same value
exp_value = (probability_white*win) + (prob_lose*lose)
print("Expected value: ", exp_value)