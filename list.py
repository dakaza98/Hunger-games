from microbit import *

# A list is an ordered collection of elements.  To create a list simply place
# comma-separated elements between square brackets [ and ].

# An empty list.
e = []
e  # []

# A list with one element.
one = [127]
one  # [127]

# A list with two elements.
two = [55, 127]
two  # [55, 127]

# The elements don't have to be of the same datatype.
mix = [123, "hello", False]
mix  # [123, "hello", False]

# Each element in a list has an index. The first element has index 0, the
# second element index 1, etc.

# The individual element in a list can be accessed using index.

mix[0] # 123
mix[1] # "hello"
mix[2] # False

# The function len() returns the length of a list.

len(e)   # 0
len(one) # 1
len(two) # 2
len(mix) # 3

# A list of numbers

numbers = [1, 2, 1, 1, 3]
numbers  # [1, 2, 1, 1, 3]

# An element can be appended to the end of list using append().

numbers.append(5)
numbers  # [1, 2, 1, 1, 3, 5]

# The first occurence of an element can be removed from 
# a list using remove().

numbers.remove(1)
numbers  # [2, 1, 1, 3, 5]

# A list with images.

icons = [Image.HAPPY, Image.SAD, Image.HEART]

# Use for-in to loop through all elements of a list, from the first to the last
# element.

# Show all icons in the list icons on the display. 

for icon in icons:
    display.show(icon)
    sleep(1000)
