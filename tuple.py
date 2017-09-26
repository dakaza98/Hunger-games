from microbit import *

# A tuple is an ordered collection of elements.  To create a tuple simply place the
# comma-separated elements between ordinary parentheses ( and ).

# An empty tuple.
e = ()

# A tuple with one element.
one = (127)

# A tuple with two elements.
two = (55, 127)

# The elements don't have to be of the same datatype.
mix = (123, "hello", False)

# Each element in a tuple has an index. The first element has index 0, the
# second element index 1, etc.

# The individual element in a tuple can be accessed using index.

mix[0] # 123
mix[1] # "hello"
mix[2] # False

# A tuple with images.

icons = (Image.HAPPY, Image.SAD, Image.HEART)

# A tuple cannot be changed. Elements can be appended to a 
# list but elements cannot be added to a tuple. 

# Use for-in to loop through all elements of a tuple, from the first to the last
# Use for-in to loop through all elements of a tuple, from the first to the last
# element.

# Show all icons in the tuple icons on the display. 

for icon in icons:
    display.show(icon)
    sleep(1000)
