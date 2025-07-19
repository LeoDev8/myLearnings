# Linked List

class Link:
    """
    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.rest.rest is Link.empty
    True
    """
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link(' + repr(self.first) + rest_str + ')' 
    def __str__(self):
        return '{0} -> {1}'.format(self.first, self.rest)

def range_link(start, end):
    """Return a Link containing consecutive integers from start to end.
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))

def map_link(f, s):
    """Return a Link that contains f(x) for each x in Link s.
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s == Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """Return a Link that contains only the elements x of Link s which f(x) is a true value.
    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s == Link.empty:
        return s
    else:
        return Link(s.first, filter_link(f, s.rest)) if f(s.first) else filter_link(f, s.rest)














square = lambda x: x * x
odd = lambda x: x% 2 == 1 
