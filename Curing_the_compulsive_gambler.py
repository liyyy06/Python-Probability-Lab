# Fifty Challenging Problems in Probability by Frederick Mosteller

# Question07
# Mr. Brown always bets a dollar on the number 13 at roulette against the advice of Kind Friend. 
# To help cure Mr. Brown of playing roulette, 
# Kind Friend always bets Brown $20 at even money that Brown will be behind at the end of 36 plays. 
# How is the cure working? 
# (Most American roulette wheels have 38 equally likely numbers. 
# If the player's number comes up, he is paid 35 times his stake 
# and gets his original stake back; otherwise he loses his stake.) 

# win = +$35
# lose = -$1

total = 38
brown_num = 1
other = 37
probbrownnum = brown_num/total # 1/38
otherbrownnum = other/total # 37/38
print("Probability of Mr. Brown win: ", round(probbrownnum*100, 2), "%") # 2.63%
print("Probability of Mr. Brown lose: ", round(otherbrownnum*100, 2), "%") # 97.37%

# Expected value
ex_value = 35*probbrownnum + -1*otherbrownnum # -$1/19
plays36 = 36*ex_value # -$1.89
print("Expected value per play: ", "$", round(ex_value, 3)) # -$0.053
print("Expected value after 36 plays: ", "$", round(plays36, 3))  # -$1.894

# if Mr. Brown never win = lost $36
# 1 time win = +$35, 35 lose = -$35
# win>2 = untung
# Mr. Brown will be behind at the end of 36 plays if he never win

behind = (other/total)**36 # 0.3828
not_behind = 1 - behind # 0.6172
print("Probability of Mr. Brown will be behind at the end of 36 plays: ", round(behind*100, 2), "%") # 38.28%

ex_value1 = 20*not_behind - 20*behind # +$4.69
print("Expected value of Kind friend and Mr. Brown stake: ", "$", round(ex_value1, 2)) # +4.69

# How is the cure working
final_exvalue = plays36 + ex_value1 # +$2.79
print("Total expected value: ", "$", round(final_exvalue, 2)) # +$2.79

# Mr. Brown = +$2.79