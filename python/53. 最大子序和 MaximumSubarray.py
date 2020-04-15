import time
import random

def maxSubArray(nums):
    maxSum = nums[0]
    for i in range(1,len(nums)):
        nums[i] = max(nums[i-1],0) + nums[i];
        maxSum = max(maxSum,nums[i]);
    return maxSum

def maxSubArray2(nums):
    # 每个当前位置的最大值数列的构成是前一个最大子数列、和该位置的数字。
    maxpre = maxSum = nums[0]
    for i in range(1,len(nums)):
        # 更新下一次的最大子数列，同时也是本次的最大值
        maxpre = max(nums[i],maxpre+nums[i])
        # 本次的最大值和之前的最大值比较,得到最大值
        maxSum = max(maxpre,maxSum)
    return maxSum

def maxSubArray3(nums):
    start = end = 0
    flag = 0
    maxpre = maxSum = nums[0]
    for i in range(1,len(nums)):
        if nums[i] >= maxpre+nums[i]:
            maxpre = nums[i]
            flag = 0
        else:
            maxpre = maxpre+nums[i]
            flag = 1
        if maxpre >= maxSum:
            maxSum = maxpre
            if flag == 1:
                end = i
            if flag == 0:
                start = i
        else:
            maxSum = maxSum

    print(start,end)
    return maxSum

if __name__ == "__main__": 
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    start = time.time()
    print(maxSubArray(nums))
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray2(nums))
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray3(nums))
    print("searchInsert use time {0:.10f} s".format(time.time()-start))