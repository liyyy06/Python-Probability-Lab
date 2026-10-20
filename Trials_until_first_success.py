# Fifty Challenging Problems in Probability by Frederick Mosteller

# Question04
# On the average, how many times must a dice be thrown until one gets a 6?

# Probability getting (6) in one throw = p = 1/6
# E[X] = 1/p = 1/1/6 = 6 

import random

rolls = 0
dice = 0

while dice != 6:
    dice = random.randint(1, 6)
    rolls = rolls + 1

print("Number of rolls:", rolls)
