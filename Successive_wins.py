# Fifty Challenging Problems in Probability by Frederick Mosteller

# Question02
# To encourage Elmer's promising tennis career, 
# his father offers him a prize, 
# if he wins (at least) two tennis sets in a row in a three-set series 
# to be played with his father  and the club champion alternately: father-champion-father 
# or champion-father-champion, 
# according to Elmer's choice. 
# The champion is a better player than Elmer's father. 
# Which series should Elmer choose?

# f = Probability menang lawan Father
# c = Probability menang lawan Club champion
# f>c 

# father-champion-father
# 1st scenario (win-win-win)
# P(WWW) = f*c*f = f**2 * c
# 2nd scenario (win-win-lose)
# P(WWL) = f*c*(1-f) 
# 3rd scenario (lose-win-win)
# P(LWW) = (1-f)*c*f 
# Probability(fcf) = f**2 * c + f*c*(1-f) + (1-f)*c*f  = f*c*(2-f)

# champion-father-champion
# 1st scenario (win-win-win)
# P(WWW) = c*f*c = c**2 * f
# 2nd scenario (win-win-lose)
# P(WWL) = c*f*(1-c)
# 3rd scenario (lose-win-win)
# P(LWW) = (1-c)*f*c
# Probability(cfc) = c**2 * f + c*f*(1-c) + (1-c)*f*c = f*c*(2-c)

# f > c
# (2-c) > (2-f) 
# f*c*(2-c) > f*c*(2-f) 

# Take random number (f>c)
f = 0.6
c = 0.4

fcf = f * c * (2-f)
cfc = f * c * (2-c)

print("Probabilitas kemenangan dalam skenario father-champion-father: ", fcf)
print("Probabilitas kemenangan dalam skenario champion-father-champion: ", cfc)

# champion-father-champion is the best choice