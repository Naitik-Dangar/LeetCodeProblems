import util

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbols = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
            (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"),
            (4, "IV"), (1, "I")
        ]

        result = ""

        for value, symbol in symbols:
            count = num // value
            result += (symbol * count)
            num %= value

        return result

def testCase(x):
    print("Input:\nx = ")
    print(x)
    
    testSol = Solution()
    output = testSol.intToRoman(x)
    print("Output: ")
    print(output)

util.printCaseHeader(1)
testCase(3749)
util.printCaseHeader(2)
testCase(58)
util.printCaseHeader(3)
testCase(1994)
