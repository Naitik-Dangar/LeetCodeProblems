class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap and hashmap[compliment] != i:
                return[i, hashmap[compliment]]
        
        return[]

# this is a test

def testCase(inputList, target):
    print("Input:\nnums = ")
    print(inputList)
    print("target = ")
    print(target)
    
    testSol = Solution()
    outputList = testSol.twoSum(inputList, target)
    print("Output: ")
    print(outputList)

print("-----------------testCase1-----------------")
testCase([2,7,11,15], 9)
print("-----------------testCase2-----------------")
testCase([3,2,4], 6)
print("-----------------testCase3-----------------")
testCase([3,3], 6)
