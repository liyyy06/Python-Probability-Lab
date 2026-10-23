# Fifty Challenging Problems in Probability by Frederick Mosteller

# Question06
# Chuck-a-Luck is a gambling game often played at carnivals and gambling houses. 
# A player may bet on anyone of the numbers I, 2, 3, 4, 5, 6. 
# Three dice are rolled. 
# If the player's number appears on one, two, or three of the dice, 
# he receives respectively one, two, or three times his original stake plus his own money back; 
# otherwise he loses his stake. 
# What is the player's expected loss per unit stake? 
# (Actually the player may distribute stakes on several numbers, 
# but each such stake can be regarded as a separate bet.) 

# appear 1 time = +1 unit
# appear 2 times = +2 unit
# appear 3 times = +3 unit
# appear 0 time = -1 unit

total_number = 6
prob1 = 1
prob_others = 5

# Probability of the number appears 1 time 
Prob1 = 3 * prob1/total_number * prob_others/total_number * prob_others/total_number
print("Probability of player's number appear 1 time: ", Prob1*100, "%")

# Probability of the number appears 2 times
Prob2 = 3 * prob1/total_number * prob1/total_number * prob_others/total_number
print("Probability of player's number appear 2 times: ", Prob2*100, "%")

# Probability of the number appears 3 times
Prob3 = prob1/total_number * prob1/total_number * prob1/total_number
print("Probability of player's number appear 3 times: ", Prob3*100, "%")

# Probability of the number appears 0 time
Prob0 = prob_others/total_number * prob_others/total_number * prob_others/total_number
print("Probability of player's number appear 0 time: ", Prob0*100, "%")

# Expected value = unit * probability
exloss = 1 * Prob1 + 2 * Prob2 + 3 * Prob3 + -1 * Prob0
print("Player's expected loss per-unit stake: ", exloss)