def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """



def rec(x, y):
    if y > 0:
        return x * rec(x, y - 1)
    return 1
#rec(3, 2)


##Define a function make fn repeater which takes in a one-argument function
##f and an integer x. It should return another function which takes in one
##argument, another integer. This function returns the result of applying f to
##x this number of times.
##Make sure to use recursion in your solution.

def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(n):
        if n == 0:
            return __________________
        else:
            return __________________
    return repeat(__)

def hailstone(n):
    """
    Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    First, pick a positive integer n as the start. If n is even, divide it by 2. 
    If n is odd, multiply it by 3 and add 1. 
    Repeat this process until n is 1. 
    Returns the number of steps.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> 
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n%2 == 0: #if n is even (previous number was odd)
        print((hailstone(n)//2))
    else:
        print((hailstone(n)*3)+1)


##
##def merge(n1, n2):
##    """ Merges two numbers
##    >>> merge(31, 42)
##    4321
##    >>> merge(21, 0)
##    21
##    >>> merge (21, 31)
##    3211
##    """
##
##def make_func_repeater(f, x):
##    """
##    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
##    >>> incr_1(2) #same as f(f(x))
##    3
##    >>> incr_1(5)
##    6
##    """
##
##    def repeat(___________________):
##
##        if _______________________:
##
##           return __________________
##
##        else:
##
##           return __________________
##
##    return _________________________
##
##
##
##
##def is_prime(n):
##    """
##    >>> is_prime(7)
##    True
##    >>> is_prime(10)
##    False
##    >>> is_prime(1)
##    False
##    """
##    def prime_helper(____________________):
##        if ________________________:
##            ________________________
##        elif ________________________:
##            ________________________
##        else:
##            ________________________
##    return __________________________


