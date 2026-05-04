import util

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        sign = 1
        dig = 0
        num = 0

        # ignore whitespace
        while s[i] == " ":
            i += 1

        # determine the sign
        if s[i] == '-':
            sign = -1
            i += 1

        
        while i < len(s) and s[i].isdigit():
            dig = int(s[i])

            num = num * 10 + dig
            i += 1

        return sign * num


def testCase(s):
    print("Input:\ns = ")
    print(s)
    
    testSol = Solution()
    output = testSol.myAtoi(s)
    print("Output: ")
    print(output)

util.printCaseHeader(1)
testCase("42")
util.printCaseHeader(2)
testCase("   -042")
util.printCaseHeader(3)
testCase("1337c0d3")
