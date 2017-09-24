from microbit import *

# A set with 2-tuples (x, y) with positions on the display. 
positions = set([(2, 2), (0, 0), (4, 4)])
 
# Loop through all 2-tuples with positions. 

for position in positions:
    
    # Light up the position on the display.
    display.set_pixel(position[0], position[1], 5)
