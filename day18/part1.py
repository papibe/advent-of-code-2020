def solution(filename):

    def getLines(filename):
        with open(filename, 'r') as fp:
            data = fp.read().splitlines()
        return data


    def getTokens(inputString):
        tokens = []
        for c in inputString:
            if c != ' ':
                tokens.append(c)
        return tokens


    def isNumber(token):
        return token.isnumeric()


    def isOperator(token):
        return token in ['+', '*']


    def isOpenParen(token):
        return token == '('


    def isCloseParen(token):
        return token == ')'


    def syntaxParsing(tokens):
        output = []
        operators = []
        for token in tokens:

            if isNumber(token):
                output.append(token)    # push
                continue

            if isOperator(token):
                while operators and (not isOpenParen(operators[-1])):
                    operator = operators.pop()
                    output.append(operator)

                operators.append(token)
                continue

            if isOpenParen(token):
                operators.append(token)
                continue

            if isCloseParen(token):
                while not isOpenParen(operators[-1]):
                    operator = operators.pop()
                    output.append(operator)

                if isOpenParen(operators[-1]):
                    operators.pop() # discard open parenthesis
                else:
                    print('parenthesis mismatch', operators[-1])

        while operators:
            operator = operators.pop()
            output.append(operator)

        return output


    def evalRPN(rpn):
        estack = [] # eval stack
        for token in rpn:
            if isNumber(token):
                estack.append(token)    # push
            else:
                leftValue = estack.pop()
                rightValue = estack.pop()
                if token == '+':
                    expression = int(leftValue) + int(rightValue)
                else:
                    expression = int(leftValue) * int(rightValue)
                estack.append(str(expression))

        return int(estack.pop())


    data = getLines(filename)

    summation = 0
    for line in data:
        tokens = getTokens(line)
        rpn = syntaxParsing(tokens)
        value = evalRPN(rpn)
        summation += value

    return summation


if __name__ == "__main__":
    print(solution("./inputs/example1.txt"))    # 71
    print(solution("./inputs/example2.txt"))    # 51
    print(solution("./inputs/example3.txt"))    # 26
    print(solution("./inputs/example4.txt"))    # 437
    print(solution("./inputs/example5.txt"))    # 12240
    print(solution("./inputs/example6.txt"))    # 13632
    print(solution("./inputs/input.txt"))
