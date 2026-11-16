class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana = {}
        
        if len(s) != len(t):
            return False

        for i in s:
            ana[i] = ana.get(i, 0) + 1

        for c in t:
            if ana.get(c) == 0:
                return False
            ana[c] = ana.get(c,0) - 1
            
            if ana.get(c)< 0:
                return False

        return True

            
