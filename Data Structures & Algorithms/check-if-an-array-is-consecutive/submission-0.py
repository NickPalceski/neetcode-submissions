class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        has_no_duplicates = len(set(nums)) == len(nums)
        has_correct_range = max(nums) - min(nums) + 1 == len(nums)

        return has_no_duplicates and has_correct_range