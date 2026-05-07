import util

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        h = 0
        w = 0

        for i in range(len(height)):
            for j in range(i, len(height)):
                if height[i] <= height[j]:
                    h = height[i]
                else:
                    h = height[j]
                
                w = j - i

                if max < (h * w):
                    max = (h * w)
                
        return max

def testCase(x):
    print("Input:\nx = ")
    print(x)
    
    testSol = Solution()
    output = testSol.maxArea(x)
    print("Output: ")
    print(output)

util.printCaseHeader(1)
testCase([1,8,6,2,5,4,8,3,7])
util.printCaseHeader(2)
testCase([1,1])
