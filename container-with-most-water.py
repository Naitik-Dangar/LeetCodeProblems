import util

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1

        most = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left

            most = max(most, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return most

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
