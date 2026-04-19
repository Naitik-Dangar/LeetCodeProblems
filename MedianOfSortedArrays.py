import math
import util

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median = 0.0
        mergedList = nums1 + nums2
        mergedList.sort()


        # If list has odd number of elements
        if len(mergedList) % 2 != 0:
            index = math.floor(len(mergedList) / 2)
            median = mergedList[int(index)]
        else: # If list has even number of elements 
            index1 = int(len(mergedList) / 2)
            index2 = index1 - 1
            median = (mergedList[index1] + mergedList[index2]) / 2.0
        
        return median

def testCase(nums1, nums2):
    print("Input:\nnums1 = ")
    print(nums1)
    print("nums2 = ")
    print(nums2)
    
    testSol = Solution()
    output = testSol.findMedianSortedArrays(nums1, nums2)
    print("Output: ")
    print(output)

util.printCaseHeader(1)
testCase([1,3], [2])
util.printCaseHeader(2)
testCase([1,2], [3,4])
