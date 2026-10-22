# Fifty Challenging Problems in Probability by Frederick Mosteller

# Question05
# in a common carnival game a player tosses a penny from a distance of about 5 feet 
# onto the surface of a table ruled in I-inch squares. 
# If the penny (3/4 inch in diameter) falls entirely inside a square, 
# the player receives 5 cents but does not get his penny back; 
# otherwise he loses his penny. 
# If the penny lands on the table, what is his chance to win? 

side = 1
total_area = side * side
print("Total square area: ", total_area)

coin_diameter = 3/4
coin_radius = coin_diameter / 2
print("Coin diameter: ", coin_diameter)
print("Coin radius: ", coin_radius)

safe_length = side - coin_radius - coin_radius
safe_width = side - coin_radius - coin_radius
print("Safe length: ", safe_length)
print("Safe width: ", safe_width)

safe_area = safe_length * safe_width
print("Safe area: ", safe_area)

probability = (safe_area / total_area) * 100
print("His chance to win: ", probability, "%")