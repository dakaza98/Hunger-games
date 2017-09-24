from microbit import *
from random import randint

def bang(delay=85):
    """
    Side effects: Shows a simple but attractive animation on the display.
    
    Argument: 
      delay - paus (ms) between each image of the animation (default = 85).
    """
    
    # TODO: Add code here.
    
    
def bangs(n=3, delay=85):
    """
    Side effects: Shows the bang() animation on the display. 
    
    Arguments: 
      n - number of times to repeat the animation.
      delay - paus (ms) betwwen each image of the animation (default = 85).
    """
    
    # TODO: Add code here.
    

def flash(x, y, delay=90):
    """
    Side effects: Make position (x, y) on the display flash once. 
    
    Arguments: 
      x - x-position on the display.
      y - y-position on the display. 
      delay- time (ms) between on and off (default = 90).
    """
    
    # TODO: Add code here. 
    

def random_point():
    """
    Returns a random point (x, y) on the map. 
    """
        
    return (randint(0, 4), 2)

def add_random_point(s):
    """
    Side effects: Adds a random point to the set s. 
    """ 
    
    # Generate a random point.
    p = random_point()
    
    # TODO: Add code here to make sure a new unique element 
    # is added to the set s.
    
    
    # Add the point p to the set s.
    s.add(p)
    
    
def add_random_points(n, s):
    """
    Side effects: Add n random points to the set s.
    """
    
    for _ in range(n):
        add_random_point(s)


def spawn_hero_and_food(n, s):
    """
    Generates n random food positions and a random hero position 
    such that the hero is not on the same postion as any food. 
    
    Arguments: 
      n - Amount of food to generate.
      s - Set that will hold the generated food positions.
      
    Side effects:
      If the set s is not empty, all elements in s are removed. 
      Next n random points are added to the set s. 
    
    Return value: a random position for the hero such that. 
    """
    
    # Remove all elements (if any) from the set s. 
    s.clear()
    
    # Food may not be placed on the same spot as the hero. 
    
    # First we generate n + 1 random positions, 
    # n for the food and one for the hero all in set s. 
    
    add_random_points(n+1, s)
    
    # Take out an arbitrary element from the set s 
    # and use for the hero.
    p = s.pop()
    
    # Return the hero position.
    return p
    
def spawn(n, food):
    """
    Arguments: 
      n - Amount of food to generate.
      s - Set that will hold the generated food positions.
      
    Side effects:
      If the set s is not empty, all elements in s are removed. 
      Next n random points are added to the set s. 
      
      Shows an animation on the display. 
    
    Return value: a random position for the hero. 
    """
    
    p = spawn_hero_and_food(n, food)
    
    # Show animtion.
    bangs()
    
    # Light up all food positions on the display. 
    for (x, y) in food:
        display.set_pixel(x, y, 5)
        
    return p

def empty(s):
    """
    Returns True if the set s is empty and otherwise returns False. 
    """
    
    return len(s) == 0


food = set() # An empty set used to store the food positions. 

# Initial none random position of the hero. 
(x, y) = (2, 2)

# TODO: To enable the event loop, change False to True.

while False:    
   
   # Make the hero flash.
   flash(x, y)
       
   if button_a.was_pressed():
       x = x # TODO: Change this.
   elif button_b.was_pressed():
       y = y # TODO: Change this.
