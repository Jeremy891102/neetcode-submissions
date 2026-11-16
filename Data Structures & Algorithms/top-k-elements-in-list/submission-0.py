class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            
        res = defaultdict(int)

        for s in nums:
            res[s] += 1
        sorted_keys = sorted(res.keys(), key=lambda x: res[x])
        top_k_keys = sorted_keys[-k:]
        return top_k_keys
            