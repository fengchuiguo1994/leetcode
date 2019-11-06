class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        mydict = {}
        for i,j in enumerate(nums):
            mydict[j] = i
        for i,j in enumerate(nums):
            if target-j in mydict and mydict[target-j] != i:
                return [i,mydict[target-j]]
# Solution().twoSum.__annotations__

def towSum(nums,target):
    mydict = {}
    for i,j in enumerate(nums):
        mydict[j] = i
    for i,j in enumerate(nums):
        if target-j in mydict and mydict[target-j] != i:
            return [i,mydict[target-j]]

import time
be = time.time()

nums = [2, 7, 11, 15]
target = 9
print(towSum(nums,target))
print("use time {0:.10f} s".format(time.time()-be))