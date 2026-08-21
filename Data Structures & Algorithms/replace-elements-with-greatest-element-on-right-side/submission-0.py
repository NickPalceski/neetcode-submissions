class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #reverse iteration
        #starting max = -1
        #new max = max(oldMax, arr[i])

        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr