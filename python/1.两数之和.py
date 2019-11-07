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

# 抄袭的最快代码:(边遍历边存储字典中边判断)
class Solution:
     def twoSum(self, nums, target):
            d = {}
            for i, num in enumerate(nums):
                if target - num in d:
                    # 如果目标值减去该num的值在d的键值对里，则返回d[num]=i中的i，如果不存在，则使d[num]=i
                    return d[target - num], i
                d[num] = i