"""Generalization"""

def make_adder(n):
    """
    Return a fucntion that takes one parameter K and returns K plus N
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder
