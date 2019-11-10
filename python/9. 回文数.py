class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return int("".join(reversed(list(str(x))))) == x
        # return reversed(str(x)) == str(x)
            
aa = 121
bb = [3,4]
print(Solution().isPalindrome(aa))
