class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        ana = []

        for i in strs:
            if len(strs)==1:
                return [[i]]
            key = str(sorted(i))
            if key not in ans:
                ans[key]=[]
            ans[key].append((i)) 

        return list(ans.values())

                
            
        
        