class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out, res = [], 1
        for i in range(len(nums)): 
            for j in range(len(nums)):
                if j != i:
                    res = res * nums[j]
            out.append(res)
            res = 1
        return out
        
            
        