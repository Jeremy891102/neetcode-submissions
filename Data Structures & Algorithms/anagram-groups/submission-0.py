class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        for i in range(len(strs)):
            if any(strs[i] in group for group in output):
                continue
            group=[strs[i]]
            for j in range(len(strs)-1,i,-1):
                if sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
            output.append(group)
        return output