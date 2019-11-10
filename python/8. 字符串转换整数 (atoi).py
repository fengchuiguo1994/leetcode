class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        if re.search("^\s*[-?\+?]?\d+",str):
            tmp = int(re.search("^\s*[-?\+?]?\d+",str)[0])
        else:
            tmp = 0
        if tmp > 2**31-1:
            return 2**31-1
        elif tmp < -2**31:
            return -2**31
        else:
            return tmp
            
aa = " +987"
bb = [3,4]
print(Solution().myAtoi(aa))
