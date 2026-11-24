class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for pos, val in enumerate(nums):
            
            if val in seen:
                return [seen[val], pos]
            
            res = target - val
            seen[res]= pos