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
