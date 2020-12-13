from collections import deque

operations = {".", "+", "*"}
badDataString = "ERROR"
epsilon = "1"


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


def processCommandPlus(word: str, expression: MyExpression):
    results1, addToFirst = findLongestPrefixForExpression(word, expression.arguments[0])
    results2, addToSecond = findLongestPrefixForExpression(word, expression.arguments[1])
    return results1 + results2, addToFirst + addToSecond


def processCommandStar(word: str, expression: MyExpression):
    results, canAddMore = findLongestPrefixForExpression(word, MyExpression(".", [expression.arguments[0], expression]))
    results.append(0)
    canAddMore.append(True)
    return results, canAddMore


def processCommandConcatenation(word: str, expression: MyExpression):
    results, canAddMoreToTheLeft = findLongestPrefixForExpression(word, expression.arguments[0])
    newResults = []
    canAddMore = []
    for i in range(len(results)):
        if canAddMoreToTheLeft[i]:
            resultsFromRightSide, canAddMoreToTheRight = findLongestPrefixForExpression(word[results[i] - len(word):],
                                                                                        expression.arguments[1])
            for j in range(len(resultsFromRightSide)):
                newResults.append(results[i] + resultsFromRightSide[j])
                canAddMore.append(canAddMoreToTheRight[j])
        else:
            newResults.append(results[i])
            canAddMore.append(canAddMoreToTheLeft[i])
    return newResults, canAddMore


def processCommand(word: str, expression: MyExpression):
    if expression.operation == "+":
        results, canAddMore = processCommandPlus(word, expression)
    elif expression.operation == "*":
        results, canAddMore = processCommandStar(word, expression)
    elif expression.operation == ".":
        results, canAddMore = processCommandConcatenation(word, expression)
    return results, canAddMore


def processSymbol(word: str, expression: str):
    results = [0]
    canAddMore = [len(word) - 1 > 0]
    if word[0] == expression:
        results = [1]
    elif expression == epsilon:
        results = [0]
    else:
        canAddMore = [False]
    return results, canAddMore


def findLongestPrefixForExpression(word: str, expression):
    results = [0]
    canAddMore = [len(word) - 1 > 0]
    if isinstance(expression, MyExpression):
        results, canAddMore = processCommand(word, expression)
    if isinstance(expression, str):
        results, canAddMore = processSymbol(word, expression)
    return results, canAddMore


def findLongestPrefixForRegular(word: str, regularExpression: str):
    expression = buildExpression(regularExpression)
    if expression is badDataString:
        return badDataString
    return max(findLongestPrefixForExpression(word, expression)[0])


def readData():
    return input(), input()


if __name__ == '__main__':
    print(findLongestPrefixForRegular(*readData()))
