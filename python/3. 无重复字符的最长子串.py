class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#        length = 0
#        aa = len(s)
#        for i in range(0,aa):
#            for j in range(i,aa):
#                part = s[i:j+1]
#                if len(set(part)) == len(part):
#                    if len(part) > length:
#                        length = len(part)
#        return length
        length = 0
        subset = set()
        substr = ""
        for i in s:
            if i not in subset:
                subset.add(i)
                substr += i
            else:
                if len(subset) > length:
                    length = len(subset)
                for p,q in enumerate(substr):
                    if q == i:
                        break
                    subset.remove(q)
                substr = substr[p+1:]
                substr += i
        if len(subset) > length:
            length = len(subset)
        return length
        
aa = " "
print(Solution().lengthOfLongestSubstring(aa))