from collections import deque

operations = {".", "+", "*"}


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
    return "ERROR"


def findLongestPrefix(word="", regularExpression=""):
    print(buildExpression(regularExpression))


def readData():
    return input(), input()


if __name__ == '__main__':
    findLongestPrefix(*readData())
