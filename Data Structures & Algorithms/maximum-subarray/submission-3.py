class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        l = 0
        currSum = 0
        for r in range(len(nums)):
            
            if currSum < 0:
                currSum = 0
                l += 1
            currSum += nums[r]
            maxSub = max(maxSub, currSum)

        return maxSub