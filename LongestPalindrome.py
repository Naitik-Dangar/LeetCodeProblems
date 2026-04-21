import util

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        currentStr = ""

        for i in range(len(s)):
            currentStr = ""
            for j in range(i, len(s)):
                currentStr += s[j]
                if currentStr == currentStr[::-1]:
                    if len(currentStr) > len(longest):
                        longest = currentStr

        return longest

def testCase(s):
    print("Input:\ns = ")
    print(s)
    
    testSol = Solution()
    output = testSol.longestPalindrome(s)
    print("Output: ")
    print(output)

util.printCaseHeader(1)
testCase("babad")
util.printCaseHeader(2)
testCase("cbbd")
