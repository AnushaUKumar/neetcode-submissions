class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        if len(s) !=len(t):
            return False
        for i in range(len(s)):
            if s[i] in t:
                t.remove(s[i])
                i+=1
            else:
                return False
        return True