class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        fre = {}
        for i in nums:
            if i not in fre:
                fre[i] = 0
            fre[i]+=1
        ans = sorted(fre.items(), key=lambda p: p[1], reverse=True)

        return [ num for num, cnt in ans[:k]]
