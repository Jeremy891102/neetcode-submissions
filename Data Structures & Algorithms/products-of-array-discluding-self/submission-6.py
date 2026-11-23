class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left = [1]*n
        right = [1]*n
        ans = [1]*n
        for i in range(1,len(nums)): 
            left[i]=left[i-1]*nums[i-1]
        for j in range(-2,-len(nums)-1,-1):
            right[j] = right[j+1]*nums[j+1]

        for i in range(len(nums)):
            ans[i]= left[i]*right[i]
        return ans