class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            #left sorted portion
            if nums[l] <= nums[mid]:
                #target in right sorted portion
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    #target in left sorted portion
                    r = mid - 1
            else:
                #target in left sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    #target in right sorted portion
                    l = mid + 1
        return -1

     