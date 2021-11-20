# Problem: Implement an algorithm that convers a positive integer to binary


from stack import Stack


def intToBin(num):
    s = Stack()

    if num == 0:
        return 0

    while num > 0:
        rem = num % 2
        s.push(rem)
        num = num // 2

    res = ""
    while not s.is_empty():
        res = res + str(s.pop())

    return res