class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duo =set()

        for i in nums:
            if i in duo:
                return True
            else:
                duo.add(i)
        return False