from microbit import *

# A function is a block of organized, reusable code that is used to
# perform a single, well defined task. A function must be defined
# before it can be used.

# A function can take zero or more parameters.


# Definition of the function heart().

def heart():
    """
    This is a special multi-line comment used to document
    the function.

    Argument(s):
      This function does not depend on any parameters.

    Side effects:
      Shows the HEART icon on the display.

    Return value: None.
    """

    display.show(Image.HEART)


# Call the function heart() from the REPL ==> The HEART icon will be
# shown on the display. 
heart()


def double(n):
    """
    Argment(s):
      A number n.

    Return value: 2*n. 
    """

    # The keyword return is used to return a value
    # back to the caller of the function. 
    return 2*n


# Call the function double with 4 as argument will make double() return
# the value 8.

double(4) # Try this in the REPL ==> 8

# This will show the digit 8 on the display. 
display.show(str(double(4)))

# Parameters can be given default values.

def bing(a, b = 5):
    """
    Argument(s):
      a - number
      b - number (default 5)

    Return value: a + b.
    """

    return a + b


# Try this in the REPL ==> 10
bing(3, 7)

# Only provide the first argument ==> the default value (5) will
# be used for the second parameter.

bing(3)    # Try this in the REPL ==> 8


# Functions are a great way to split up a "big" problem into smaller problems.

def max2(a, b):
    """
    A small problem: return the largest of two values.
    """

    if a > b:
        return a
    else:
        return b


max2(2, 7) # Try this in the REPL ==> 7
max2(7, 2) # Try this in the REPL ==> 7
max2(7, 7) # Try this in the REPL ==> 7

def max3(a, b, c):
    """
    A larger problem: return the largest of three values.
    """

    # Use max2() as part of the solution of max3.
    return max2(a, max2(b, c))


max3(2, 7, 5) # Try this in the REPL ==> 7
max3(7, 5, 2) # Try this in the REPL ==> 7
max3(5, 2, 7) # Try this in the REPL ==> 7
max3(5, 5, 2) # Try this in the REPL ==> 5
max3(2, 5, 5) # Try this in the REPL ==> 5
max3(5, 2, 5) # Try this in the REPL ==> 5
max3(5, 5, 5) # Try this in the REPL ==> 5
