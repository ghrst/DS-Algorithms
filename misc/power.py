# Problem: Given two numbers b, and n calculate b raised to the n-th power recursively


def power_linear(b, n):
    """
    :type b: int
    :type n: unsigned int
    :rtype: int
    """
    if n == 0:
        return 1
    else:
        return b * power_linear(b, n - 1)


def power_neg_linear(b, n):
    """
    :type b: int
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1
    elif n > 0:
        return b * power_neg_linear(b, n - 1)
    else:
        return power_neg_linear(b, n + 1) / b


def power_log(b, n):
    """
    :type b: int
    :type n: unsigned int
    :rtype: int
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power_log(b, n // 2)**2
    else:
        return b * (power_log(b, (n - 1) // 2)**2)