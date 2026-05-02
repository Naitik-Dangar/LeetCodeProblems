import util

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        isNegative = False
        # check if number is negative
        if x < 0:
            isNegative = True

        if isNegative:
            x = x * -1
            x_string = str(x)
            rev_x = x_string[::-1]
            return int(rev_x) * -1
        else:     
            x_string = str(x)
            rev_x = x_string[::-1]

        return int(rev_x)
    

def testCase(x):
    print("Input:\nx = ")
    print(x)
    
    testSol = Solution()
    output = testSol.reverse(x)
    print("Output: ")
    print(output)

util.printCaseHeader(1)
testCase(123)
util.printCaseHeader(2)
testCase(-123)
util.printCaseHeader(3)
testCase(120)
