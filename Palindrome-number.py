import util

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev_x = 0
        num = x

        if x < 0:
            return False

        while x > 0:
            digit = x % 10

            rev_x = (rev_x * 10) + digit

            x //= 10

        return num == rev_x


def testCase(x):
    print("Input:\nx = ")
    print(x)
    
    testSol = Solution()
    output = testSol.isPalindrome(x)
    print("Output: ")
    print(output)

util.printCaseHeader(1)
testCase(121)
util.printCaseHeader(2)
testCase(-121)
util.printCaseHeader(3)
testCase(10)
