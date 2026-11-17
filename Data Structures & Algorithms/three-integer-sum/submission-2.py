class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            a = nums[i]
            target = -a
            seen = set()
            for n in nums[i+1:]:
                if target - n in seen:
                    ans.add((a,n,target-n))
                seen.add(n)
        return [list(t) for t in ans]
