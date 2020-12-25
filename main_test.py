import unittest
from unittest.mock import patch

from main import buildExpression, findLongestPrefixForRegular, MyExpression, findLongestPrefixForExpression, processCommandPlus, \
    processCommandStar, processCommandConcatenation


class MyTestCase(unittest.TestCase):
    def testBuildingExpression(self):
        self.assertEqual(str(buildExpression("acb..bab.c.*.ab.ba.+.+*a.")), "((acb+b(abc)*(ab+ba)))*a")

    def testFindLongestPrefixForExpression(self):
        ex1 = MyExpression(".", ["a", "a"])
        ex2 = MyExpression(".", ["a", ex1])
        self.assertEqual(findLongestPrefixForExpression("aaab", ex2), ([3], [True]))

    @patch('main.findLongestPrefixForExpression', return_value=([1], [False]))
    def testProcessCommandPlus(self, findLongestPrefixForExpression):
        ex = MyExpression("+", ["a", "b"])
        self.assertEqual(processCommandPlus("ab", ex), ([1, 1], [False, False]))

    @patch('main.findLongestPrefixForExpression', return_value=([1], [False]))
    def testProcessCommandStar(self, findLongestPrefixForExpression):
        ex = MyExpression("*", ["a"])
        self.assertEqual(processCommandStar("a", ex), ([1, 0], [False, True]))

    @patch('main.findLongestPrefixForExpression', return_value=([0, 1], [False, True]))
    def testProcessCommandConcatenation(self, findLongestPrefixForExpression):
        ex1 = MyExpression("+", ["a", "b"])
        ex2 = MyExpression(".", [ex1, "a"])
        self.assertEqual(processCommandConcatenation("ba", ex2), ([0, 1, 2], [False, False, True]))

    def testFindLongestPrefixForRegular(self):
        self.assertEqual(findLongestPrefixForRegular("acbac", "acb..bab.c.*.ab.ba.+.+*a."), 5)

    def test1(self):
        self.assertEqual(findLongestPrefixForRegular("aaab", "a*b."), 4)

    def test2(self):
        self.assertEqual(findLongestPrefixForRegular("abab", "ab.abc..+ab.."), 4)

    def test3(self):
        self.assertEqual(findLongestPrefixForRegular("abc", "a*b*.ab+c+.b*."), 3)

    def test4(self):
        self.assertEqual(findLongestPrefixForRegular("abc", "a*b*a*..cb+."), 3)

    def test5(self):
        self.assertEqual(findLongestPrefixForRegular("abacb", "ab+c.aba.*.bac.+.+*"), 5)

    def test6(self):
        self.assertEqual(findLongestPrefixForRegular("acbac", "acb..bab.c.*.ab.ba.+.+*a."), 5)

    def test7(self):
        self.assertEqual(findLongestPrefixForRegular("bbaab", "bb1aa...."), 4)

    def test8(self):
        self.assertEqual(findLongestPrefixForRegular("bbaab", "bb.b1+aa..."), 4)

    def testBadData1(self):
        self.assertEqual(findLongestPrefixForRegular("any word", "ab.+*...."), "ERROR")

    def testBadData2(self):
        self.assertEqual(findLongestPrefixForRegular("any word", "ab.ba."), "ERROR")


if __name__ == '__main__':
    unittest.main()
