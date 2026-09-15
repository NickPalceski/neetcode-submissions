class Solution:
    def maxDifference(self, s: str) -> int:
        # built in dict collections for hashable objects: {a : 5, b : 2, c : 1}
        count = Counter(s)
        maxOdd, minEven = 0, len(s)

        for cnt in count.values():
            if cnt & 1:
                maxOdd = max(maxOdd, cnt)
            else:
                minEven = min(minEven, cnt)
        
        return maxOdd - minEven