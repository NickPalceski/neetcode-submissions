class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] = freq.get(n,0) + 1
            else:
                freq[n] = 1
        sorted_freq = dict(sorted(freq.items(), key = lambda i: i[1], reverse = True))
        return list(sorted_freq.keys())[:k]


                
            
