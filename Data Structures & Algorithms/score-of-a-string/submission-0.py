class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        l, r = 0, 1

        while r < len(s):
            score += abs( (ord(s[r]) - ord(s[l])) )
            l, r = l + 1, r + 1
        
        return score