# Problem: This problem consists of adding two nonnegative integers a and b, where we cannot use the general arithmetic commands 
# such as addition, subtraction, multiplication, or division. Instead, we are only allowed to add or subtract single units from 
# the numbers (a constant amount of times)


def slow_addition_recur(a, b):
    """
    :type a: unsigned int
    :type b: unsigned int
    :rtype: unsigned int
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return 1 + 1 + slow_addition_recur(a - 1, b - 1)