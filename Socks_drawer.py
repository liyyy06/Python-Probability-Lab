# Fifty Challenging Problems in Probability by Frederick Mosteller

# Question01
# A drawer contains red socks and black socks. 
# When two socks are drawn at random, the probability that both are red is 1/2. 
# (a) How small can the number of socks in the drawer be? 
# (b) How small if the number of black socks is even?

# (a)
for total in range (3, 10):
    for red in range (2, total):
        black = total - red 

        if 2 * red * (red -1) == total * (total - 1):
            print("Red:", red)
            print("Black:", black)
            print("(a) Minimum number of socks:", total)

# (b)
for total in range (3, 100):
    for red in range (2, total):
        black = total - red 

        if 2 * red * (red -1) == total * (total - 1):
            if black % 2 == 0 : 
                print("Red:", red)
                print("Black:", black)
                print("(b) Minimum number of socks, if black is even:", total)
