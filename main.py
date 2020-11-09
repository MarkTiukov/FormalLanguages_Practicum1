from collections import deque

operations = {".", "+", "*"}
badDataString = "ERROR"


class MyExpression:
    def __init__(self, operation: str, arguments: list):
        self.operation = operation
        self.arguments = arguments

    def __str__(self):
        if self.operation == "*":
            return "(" + str(self.arguments[0]) + ")*"
        elif self.operation == "+":
            return "(" + str(self.arguments[0]) + "+" + str(self.arguments[1]) + ")"
        elif self.operation == ".":
            return str(self.arguments[0]) + str(self.arguments[1])


def buildExpression(expressionInReversePolishNotation: str):
    expressionStack = deque()
    for symbol in expressionInReversePolishNotation:
        if symbol not in operations:
            expressionStack.append(symbol)
            continue
        try:
            if symbol == "*":
                currentArguments = [expressionStack.pop()]
            elif symbol == "+" or symbol == ".":
                currentArguments = [expressionStack.pop(), expressionStack.pop()]
                currentArguments.reverse()
            expressionStack.append(MyExpression(symbol, currentArguments))
        except IndexError:
            return gotBadData()
    if len(expressionStack) != 1:
        return gotBadData()
    return expressionStack.pop()


def gotBadData():
    return badDataString


def findLongestPrefixForExpression(word: str, expression: MyExpression):
    result = 0
    canAddMore = True
    if isinstance(expression, MyExpression):
        if expression.operation == "+":
            result1, addToFirst = findLongestPrefixForExpression(word, expression.arguments[0])
            result2, addToSecond = findLongestPrefixForExpression(word, expression.arguments[1])
            result = max(result1, result2)
            canAddMore = addToFirst or addToSecond
        elif expression.operation == "*":
            # TODO fill * operation
            findLongestPrefixForExpression(word, MyExpression(".", [expression.arguments[0], expression]))
        elif expression.operation == ".":
            result, canAddMore = findLongestPrefixForExpression(word, expression.arguments[0])
            if canAddMore:
                resultFromRightSide, canAddMore = findLongestPrefixForExpression(word[result - len(word):],
                                                                                 expression.arguments[1])
                result += resultFromRightSide

    if isinstance(expression, str):
        if word[0] == expression:
            result = 1
    return result, canAddMore


def findLongestPrefixForRegular(word: str, regularExpression: str):
    expression = buildExpression(regularExpression)
    if expression is badDataString:
        return badDataString
    return findLongestPrefixForExpression(word, expression)


def readData():
    return input(), input()


if __name__ == '__main__':
    print(findLongestPrefixForRegular(*readData()))
