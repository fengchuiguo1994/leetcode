class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        substr = ""
        for i,j in enumerate(s):
            tmp = 0
            while True: # cabac   module
                tmp += 1
                if i-tmp < 0:
                    break
                try:
                    s[i-tmp] and s[i+tmp]
                    if s[i-tmp] == s[i+tmp]:
                        pass
                    else:
                        break
                except IndexError:
                    break
            tmp = tmp - 1
            # print(i,tmp,i-tmp,i+tmp+1,2*tmp+1)
            if 2*tmp+1 > length:
                substr = s[i-tmp:i+tmp+1]
                length = 2*tmp+1
            
            tmp = 0
            while True: # caac   module
                tmp += 1
                if i+1-tmp < 0:
                    break
                try:
                    s[i+1-tmp] and s[i+tmp]
                    if s[i+1-tmp] == s[i+tmp]:
                        pass
                    else:
                        break
                except IndexError:
                    break
            tmp = tmp - 1
            # print("----",i,tmp,i-(tmp-1),i+tmp+1,2*tmp)
            if 2*tmp > length:
                substr = s[i-(tmp-1):i+tmp+1]
                length = 2*tmp
        return substr
                
aa = "bb"
bb = [3,4]
print(Solution().longestPalindrome(aa))