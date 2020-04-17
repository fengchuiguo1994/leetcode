import time
import random

def climbStairs(n):
    if n==1:
        return 1 # 一种上去
    if n==2:
        return 2 # 两种，一步上，两次一步上
    else:
        return climbStairs(n-1)+climbStairs(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1 # 一种上去
        if n==2:
            return 2 # 两种，一步上，两次一步上
        a = 1
        b = 2
        for i in range(2,n):
            a,b = b,a+b
        return b
        
if __name__ == "__main__": 
    x = 38
    
    start = time.time()
    print(Solution().climbStairs(x))
    print("climbStairs use time {0:.10f} s".format(time.time()-start))