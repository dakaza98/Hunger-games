from microbit import * 
from random import randint 
  
# 1D051 (2017) - Programmign assignment 1 
  
# https://www.it.uu.se/education/course/homepage/introit/ht17/draft/assignment-1/ 
  
# Author: Karl Marklund <karl.marklund@it.uu.se> september 2017.  
  
# In Python all functions must be defiend before being used. Therefore the top  
# (the highest level of abstraction) is at the end of this source file and 
# the bottom (the lovest level of abstraction) is at the beginning of this  
# source file.  
  
######################################################################## 
#### Abstraction level 5 - Functions used by the level 4 functions. ####           
######################################################################## 
  
def random_point(): 
    #Returns a random point (x, y) on the map.   
    return (randint(0, 4), randint(0,4)) 
  
######################################################################## 
#### Abstraction level 4 - Functions used by the level 3 functions. ####           
######################################################################## 
  
def add_random_point(s): 
    # Argument(s): 
    #   s (set) - A set with positions (x, y) on the map. 
      
    # Side effects:  
    #   Updates the set s. 
  
    # Return value: The set s with a random point added. 

    # Generate a random point. 
    p= random_point() 
   
    while True: 
        if(not p in s):
           # Add the point p to the set s.  
           s.add(p) 
           break 
        else: 
            p = random_point()     
  
    return s 
     
######################################################################## 
#### Abstraction level 3 - Functions used by the level 2 functions. ####           
######################################################################## 
  
def bang(delay=85): 
    # Side effects: Shows a simple but attractive animation on the display. 
  
    # Argument(s): 
    #   delay - paus (ms) between each image of the animation (default = 85). 
    
    empty = Image("00000:00000:00000:00000:00000") 
    dot = Image("00000:00000:00900:00000:00000") 
    animation= [empty, dot, Image.DIAMOND_SMALL, Image.DIAMOND, empty] 
    display.show (animation, delay) 
  
def random_points(n): 
    # Creates a set with n random points (x, y). 
  
    # Argument(s): 
    #  n (integer) - Number of point to create. 
  
    # Return value: A set with n random points (x, y). 
    
    s = set() # An empty set. 
  
    for _ in range(n): 
       s = add_random_point(s) 
     
    return s 
  
######################################################################## 
#### Abstraction level 2 - Functions used by the level 1 functions. #### 
######################################################################## 
  
def bangs(n=3, delay=85): 
    # Side effects: Shows the bang() animation on the display. 
  
    # Arguments: 
    #   n - number of times to repeat the animation. 
    #   delay - paus (ms) betwwen each image of the animation (default = 85). 
    
    m=0 
    while m < n: 
        bang(delay) 
        m=m+1 
         
def spawn_hero_and_food(n): 
    # Argument(s): 
    #   n - (integer) mount of food to generate. 
  
    # Return value: A tuple (hero, food). 
    #   hero (tuple) - A random position (x, y) for the hero. 
    #   food (set)   - A set with n random positions (x, y) for the food. 
     
    # First we generate n + 1 random positions, 
    # n for the food and one for the hero all in set s. 
    s = random_points(n+1) 
     
    # Take out an arbitrary element from the set s 
    # and use for the hero. 
    hero = s.pop() 
     
    return (hero, s) 
  
def show(food): 
    # Display the food on the map. 
  
    # Argument(s): 
    #   food (set) - A set with positioins (x, y) on the map where   
    #                there is food available. 
    # Side effects: 
    #   Lights up all the positions on the display where there is 
    #   food available. 
  
    for (x,y) in food: 
        display.set_pixel(x,y,6) 
         
######################################################################## 
#### Abstraction level 1 - Functions used by event loop.            #### 
######################################################################## 
  
def eat(hero, food): 
    # If the hero is on a position on the map where there also is food, eat the 
    # food. 
  
    # Argument(s): 
    #   hero (tuple) - The position (x, y) of the hero on the map. 
    #   food (set)   - A set with positions (x, y) where there is food on the map. 
                  
                    
    # Side effects: May update the set food. 
     
    # Return value: The updated set of food on the map. 

    if hero in food: 
        food.discard(hero)
  
    return food 
  
def move(hero):     
    # Update the hero position on button presses. 
  
    # Argument(s): 
    # hero (tuple) - The current position (x, y) of the hero. 
  
    # Return values: A tuple (x, y) with the updated position of the 
    # hero. 
     
    # Tuple matching to get the x-value and y-value of the hero position. 
    (x, y) = hero 
  
    if button_a.was_pressed(): 
        x = makeMove(x) 
    elif button_b.was_pressed(): 
        y = makeMove(y) 
  
    return (x, y) 
  
def makeMove(coordinate): 
   # Moves the hero to the opposite side of the map if the hero is on the edge. 
   # Otherwise, the hero is moved one step. 
     
   # Arguments: 
   #    coordinate (integer) - The coordinate to be changed (x or y) 
     
    if(coordinate == 4): 
        coordinate = 0 
    else:         
        coordinate += 1 
        
    return coordinate 
  
def flash(hero, delay=90): 
    # Side effects: 
    #   Make the hero position flash once on the display. 
  
    # Arguments: 
    #    hero (tuple)    - Position (x, y) of the hero. 
    #    delay (integer) - Duration (ms) of light on and off (default = 100).    
     
    # Tuple matching to get the x-value and y-value of the hero position. 
    (x, y) = hero 
  
    # Makes the hero flash 
    display.set_pixel(x, y, 9) 
    sleep(delay) 
    display.set_pixel(x, y, 0) 
    sleep(delay) 
  
def spawn(n): 
    # Argument(s): 
    #   n (integer) - Amount of food to generate. 
  
    # Side effects: 
    #   Show an animation on the display. 
  
    # Return value: A tuple (hero, food). 
    #   hero (tuple) - A random position (x, y) for the hero. 
    #   food (set)   - A set with n random positions (x, y) for the food. 
  
    (hero, food) = spawn_hero_and_food(n) 
     
    # Show animation. 
    bangs(3,300) 
     
    # Light up all food positions on the display. 
    show(food) 
     
    return (hero, food) 
  
def empty(s): 
    # Argument(s): 
    #   s (set) - The set to check if it's empty
  
    # Return value: True if the set s is empty and otherwise False. 
     
    return len(s) == 0 
  
######################################################################## 
##The simplest valid state.
######################################################################## 
  
hero = (2, 2) # None random position for the hero (tuple). 
food = set()  # No food (empty set) 
  
######################################################################## 
#### Event loop.                                                    #### 
######################################################################## 
  
while True: 
  
    # If no food left, spawn new food and a random position for the hero. 
    if empty(food): 
        (hero, food) = spawn(5) 
  
    # Make the position of the hero flash. 
    flash(hero, 300) 
  
    # Update the hero position on button presses. 
    hero = move(hero) 
  
    # If the hero steps on food, eat. 
    food = eat(hero, food) 
 