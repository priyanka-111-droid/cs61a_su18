"""Midterm Review"""
from lab06 import *

# Q6
def summation(n, term):
    """Return the sum of the first n terms of a sequence.

    >>> summation(5, lambda x: pow(x, 3))
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    >>> from construct_check import check
    >>> check(LAB_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod'])
    True
    """
    "*** YOUR CODE HERE ***"
    # ITERATIVE:
    # if(n==0):
    #   return 0
    # elif(n==1):
    #   return odd_term(i)
    # else:
    #   for loop from i till n:
    #     if(i is odd):
    #       total+=odd_term(i)
    #     else:
    #       total+=even_term(i)
    #   return total 


    #RECURSIVE:
    def is_even(i):  #mutual recursion
      if(i==0):
        return True 
      return is_odd(i-1) 
    def is_odd(i):
      if(i==0):
        return False 
      return is_even(i-1) 
    
    def func(i,total): # i stands for current term
      if(n==0):
        return total 
      elif(n==1):
        return odd_term(i)
      elif(i>n):
        return total 
      elif(is_odd(i)):
        return func(i+1,total+odd_term(i))
      elif(is_even(i)):
        return func(i+1,total+even_term(i))
    return func(1,0)

# Q7
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if(m<=0 or n<=0):
      return 0
    if(m==1 or n==1):
      return 1 
    return paths(m-1,n)+paths(m,n-1)

# Q8
def insert_into_all(item, lsts):
    """Assuming that lsts is a list of lists, return a new list consisting of
    all the lists in lsts, but with item added to the front of each.

    >>> lsts = [[], [1, 2], [3]]
    >>> insert_into_all(0, lsts)
    [[0], [0, 1, 2], [0, 3]]
    """
    return [[item] + lst for lst in lsts]

def inc_subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order.

    >>> seqs = inc_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> inc_subseqs([])
    [[]]
    """
    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:],prev)
        else:
            with_first = subseq_helper(s[1:],s[0])
            without_first = subseq_helper(s[1:],prev)
            return insert_into_all(s[0],with_first) + without_first
    return subseq_helper(s, 0)

# Q9
def dict_to_lst(d):
    """Returns a list containing all the (key, value) pairs in d as two-element
    tuples ordered by increasing value.

    >>> nums = {1: 5, 2: 3, 3: 4}
    >>> dict_to_lst(nums)
    [(2, 3), (3, 4), (1, 5)]
    >>> words = {'first': 'yes', 'second': 'no', 'third': 'perhaps'}
    >>> dict_to_lst(words)
    [('second', 'no'), ('third', 'perhaps'), ('first', 'yes')]
    """
    result = []
    for _ in range(len(d)):
        pair = min(d.items(), key=lambda pair:pair[-1])
        d.pop(pair[0])
        result.append(pair)   
    return result


# Q10
def filter(pred, lst):
    """Filters lst with pred using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    "*** YOUR CODE HERE ***"

# Q11
def replace_all(d, x, y):
    """Replace all occurrences of x as a value (not a key) in d with y.
    >>> d = {3: '3', 'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {3: '3', 'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"

# Q12
def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    "*** YOUR CODE HERE ***"

# Q13
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
