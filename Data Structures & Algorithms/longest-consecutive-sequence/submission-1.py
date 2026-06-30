class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # Check if its the start of a sequence (no number before it)
            if (n - 1) not in numSet:
                length = 0
                # While there are consecutive numbers
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        