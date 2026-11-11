class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_indi = []
        t_indi = []
        for x in s:
            s_indi.append(x)
        for y in t:
            t_indi.append(y)
        s_indi.sort()
        t_indi.sort()
        if s_indi == t_indi:
            return True
        
        return False
       