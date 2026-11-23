class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for i in s:
            if i-1 in s:
                continue
            else:
                length = 1
            while i+length in s:
                length +=1
            best = max(best, length)

        return best
            