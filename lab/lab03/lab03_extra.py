""" Optional problems for Lab 3 """

# Q4
from itertools import count


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if(i==n): # if n is 2
            return True 
        if(n%i==0):
            return False
        return helper(i+1)
         
    return helper(2)


# Q5
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if(b>a):
        a,b = b,a #a is always greater than b
    if(a%b==0):
        return b
    else:
        return gcd(b, a % b)


# Q6
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def count_digit(i,n):
        # base case
        if(n<10):
            if(n==i):
                return 1
            else:
                return 0
        
        #last digit
        elif n % 10 == i:
            return 1 + count_digit(i, n//10)
        else:
            return count_digit(i, n//10)


    def helper(n):
        if(n<10):
            return 0
        return helper(n//10) + count_digit(10-n%10,n//10)
    return helper(n)

# Q7
def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    "*** YOUR CODE HERE ***"
    return [x for x in range(1,n) if n%x==0]
