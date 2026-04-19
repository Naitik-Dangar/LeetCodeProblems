import util

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        substring = ""

        for i in range(len(s)):
            if s[i] in substring:
                substring = "" + s[i]
            else:
                substring += s[i]

            if len(substring) > longest:
                longest = len(substring)
        
        return longest
    
def testCase(s: str):
    print("Input:\ns = ")
    print(s)
    
    testSol = Solution()
    output = testSol.lengthOfLongestSubstring(s)
    print("Output: ")
    print(output)

util.printCaseHeader(1)
testCase("abcabcbb")
util.printCaseHeader(2)
testCase("bbbbb")
util.printCaseHeader(3)
testCase("pwwkew")