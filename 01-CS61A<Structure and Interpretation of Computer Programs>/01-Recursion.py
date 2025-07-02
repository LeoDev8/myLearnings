def print_all(x):
    print(x)
    return print_all

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum



def split(n):
    return n // 10, n % 10
def sum_digits(n):
    if(n < 10):
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

"""
Is fact implemented correctly?

1. Verfy the base case
2. Treat fact as a functional abstraction!
3. Assume thet fact(n -1) is correct
4. Verify that fact(n) is correct, assuming that fact(n -1) correct.
"""

def fact(n):
    if(n == 0):
        return 1
    return fact(n - 1) * n

def luhn_sum(n):
    if(n < 10):
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last
def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if(n < 10):
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

















