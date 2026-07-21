class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            #initial check - full rotation, 1st value is minimum
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                #search right side
                l = mid + 1
            else:
                #search left side
                r = mid - 1
        return res