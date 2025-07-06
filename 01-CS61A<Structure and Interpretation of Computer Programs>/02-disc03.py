""" Q1: Warm Up: Recursive Multiplication
These exercises are meant to help refresh your memory of the topics covered in lecture.
Write a function that takes two numbers m and n and returns their product. Assume m and 
n are positive integers. Use recursion, not mul or *.
"""
def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if m == 0 or n == 0:
        return 0
    return n + multiply(m - 1, n)

""" Q2: Swipe
Implement swipe, which prints the digits of argument n, one per line, first backward 
then forward. The left-most digit is printed only once. Do not use while or for or str. 
(Use recursion, of course!)
"""
def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n % 10)
        swipe(n // 10)
        print(n % 10)


""" Q3: Skip Factorial
Define the base case for the skip_factorial function, which returns the product of every 
other positive integer, starting with n.
"""
def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 0:
        return 1
    else:
        return n * skip_factorial(n - 2)

""" Q4: Recursive Hailstone
Recall the hailstone function from Homework 1. First, pick a positive integer n as the start. 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. 
Repeat this process until n is 1. Complete this recursive version of hailstone 
that prints out the values of the sequence and returns the number of steps.
"""
def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return hailstone(n // 2) + 1

def odd(n):
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    return hailstone(3 * n + 1) + 1
        
"""Q5: Count Stair Ways
Imagine that you want to go up a flight of stairs that has n steps, where n is a positive integer. 
You can take either one or two steps each time you move. In how many ways can you go up 
the entire flight of stairs?

You'll write a function count_stair_ways to answer this question. Before you write any code, consider:

How many ways are there to go up a flight of stairs with n = 1 step? 
What about n = 2 steps? Try writing or drawing out some other examples and see if you notice any patterns.
What is the base case for this question? What is the smallest input?

Now, fill in the code for count_stair_ways:
"""
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either one step or two steps at a time.
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        """
        1. First step is 2: count_stair_ways(n - 2)
        2. First step is not 2: count_stair_ways(n - 1)
        """
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

""" Q6: Subsequences
A subsequence of a sequence S is a subset of elements from S, in the same order they appear in S. Consider 
the list [1, 2, 3]. Here are a few of its subsequences [], [1, 3], [2], and [1, 2, 3].

Write a function that takes in a list and returns all possible subsequences of that list. The subsequences 
should be returned as a list of lists, where each nested list is a subsequence of the original input.

In order to accomplish this, you might first want to write a function insert_into_all that takes an item 
and a list of lists, adds the item to the beginning of each nested list, and returns the resulting list.
"""
def insert_into_all(item, nested_list):
    """Return a new list consisting of all the lists in nested_list,
    but with item added to the front of each. You can assume that
    nested_list is a list of lists.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    "*** YOUR CODE HERE ***"
    return [item] + nested_list

def subseqs(s):
    """Return a nested list (a list of lists) of all subsequences of S.
    The subsequences can appear in any order. You can assume S is a list.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    if len(s) == 0:
        return [[]]
    else:
        rest_subseq = subseqs(s[1:])
        return [[s[0]] + seq for seq in rest_subseq] + rest_subseq

if __name__ == "__main__":
    # print(multiply(4, 8))
    # swipe(2837)
    # print(skip_factorial(5), skip_factorial(8))
    # a = hailstone(1)
    # print(a)
    # b = hailstone(10)
    # print(b)
    # print(count_stair_ways(5), count_stair_ways(4))
    seqs = subseqs([1, 2, 3])
    print(sorted(seqs))
