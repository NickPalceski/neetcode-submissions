class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, last = len(s) - 1, 0
        
        while s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            last += 1
            i -= 1
        
        return last
