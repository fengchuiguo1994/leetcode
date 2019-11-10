class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        p = "^"+p+"$"
        print(p)
        return re.match(p,s)
            
aa = "aa"
bb = "a*"
print(Solution().isMatch(aa,bb))
