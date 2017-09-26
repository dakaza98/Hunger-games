from microbit import *

# A set is an unordered collection of unique elements. 

# An empty set.
e = set()
e  # {}

# A none empty set is created by using a list of
# elements as argument to set().

# A set with one element. 
one = set([1])
one  # {1}

# A set with  two elements.
two = set([5, 7])
two  # {7, 5} 

# NOTE: Sets are unordred. When the REPL prints a set the
# order of the elements are undefined.

# The function len() returns the number of elements in a set.

len(e)   # 0
len(one) # 1
len(two) # 2

# Elements can be added to a set using add().

s = set([2, 7, 3])
s  # {7, 2, 3} 

s.add(5)
s  # {7, 2, 3, 5}

# Adding an element already in the set does not change the set. 
s.add(3)
s  # {7, 2, 3, 5}

# The method remove() removes an element from a set. 
s.remove(2)
s  # {7, 3, 5}

# Test if an element is a member of a set.

7 in s # True
2 in s # False
3 in s # True
5 in s # True
9 in s # False

# Use for-in to loop through all elements of a set. However, 
# since sets are unordered, it is undefined which order the 
# iteration will follow.

# Show all numbers in the set s on the display. 

for n in s:
    display.show(str(n))
    sleep(1000)
    
 

