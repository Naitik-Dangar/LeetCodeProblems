import util

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
    
        for i in range(len(strs[0])):
            char = strs[0][i]

            for s in strs[1:]:

                if i == len(s) or s[i] != char:
                    return strs[0][:i]
                
        return strs[0]

def testCase(strs):
    print("Input:\nstrs = ")
    print(strs)
    
    testSol = Solution()
    output = testSol.longestCommonPrefix(strs)
    print("Output: ")
    print(output)

util.printCaseHeader(1)
testCase(["flower", "flow", "flight"])
util.printCaseHeader(2)
testCase(["dog", "racecar", "car"])
