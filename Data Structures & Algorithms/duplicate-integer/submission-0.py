class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if nums.count(i) > 1:
                print(nums.index(i))
                return True
            else:
                continue
        return False    