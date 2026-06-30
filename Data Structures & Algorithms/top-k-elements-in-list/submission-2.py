class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #keep track of count in Map
        count = {}
        #keep track of freq in list
        freq = [[] for i in range(len(nums)+1)]
        # Add each num to Map key and its frequency as value (num:freq)
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        #For each pair (num and count) populate the freq list
        for n, c in count.items():
            freq[c].append(n)
        #Loop freq list backward and append to result top K elements
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


                
            
