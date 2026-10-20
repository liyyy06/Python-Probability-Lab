# Fifty Challenging Problems in Probability by Frederick Mosteller

# Question03
# A three-man jury has two members each of whom independently has probability p of making the correct decision 
# and a third member who flips a coin for each decision (majority rules). 
# A one-man jury has probability p of making the correct decision. 
# Which jury has the better probability of making the correct decision?

# one-man jury = p
# three-man jury = p-p-1/2 (coin)

# correct decision = c
# wrong decision = w

p = 0.8 # randomly choose (80%)

# three-man jury
# 4 scenario
# (1) C - C - C = correct 
first_scenario = p * p * 1/2 
# (2) C - C - W = correct 
second_scenario = p * p * 1/2
# (3) C - W - c = correct  
third_scenario = p * (1-p) * 1/2 
# (4) W - C - C = correct 
forth_scenario = (1-p) * p * 1/2
p_correct = first_scenario + second_scenario + third_scenario + forth_scenario

one_jury = p
three_jury = p_correct

print("One-man jury:", one_jury)
print("Three-man jury:", three_jury)

# Both has the same probability of making a correct decision
