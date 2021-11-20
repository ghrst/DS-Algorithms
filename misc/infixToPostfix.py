# Problem: Assume the infix expression is a string of tokens delimited by spaces. The operator tokens are *, /, +, and −, along 
# with the left and right parentheses, ( and ). The operand tokens are the single-character identifiers 𝐴, 𝐵, 𝐶, and so on. Write
# an algorithm that converts the infix expression to postfix



from stack import Stack


def infixToPostfix(expr):
    opStack = Stack()
    results = []
    input = expr.split(' ')
    operandTokens = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    opPrecedence = {'*':3, '/':3, '+':2, '-':2, '(':1}

    for token in input:
        if token in operandTokens:
            results.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            t = opStack.pop()
            while t != '(':
                results.append(t)
                t = opStack.pop()
        else:
            while not opStack.is_empty() and opPrecedence[opStack.top()] >= opPrecedence[token]:
                results.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        results.append(opStack.pop())

    return " ".join(results)


# print(infixToPostfix("( A + B ) * ( C + D )"))
# print(infixToPostfix("( A + B ) * C"))
# print(infixToPostfix("A + B * C"))