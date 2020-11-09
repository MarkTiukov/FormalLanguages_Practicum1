import unittest

from main import findLongestPrefixForRegular, buildExpression


class MyTestCase(unittest.TestCase):
    def testBuildingExpression(self):
        self.assertEqual(str(buildExpression("acb..bab.c.*.ab.ba.+.+*a.")), "((acb+b(abc)*(ab+ba)))*a")

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
