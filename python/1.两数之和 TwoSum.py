import time
import random

def method1(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]: # can be drop
                continue
            if nums[i] + nums[j] == target:
                print(nums[i],nums[j],target)
                return [i,j]

def method2(nums,target):
    mydict = {}
    for i,j in enumerate(nums):
        mydict[j] = i
    for i,j in enumerate(nums):
        if target-j in mydict and mydict[target-j] != i:
            print(nums[i],nums[mydict[target-j]],target)
            return [i,mydict[target-j]]
        
def method3(nums,target):
    mydict = {}
    for i,num in enumerate(nums):
        if target-num in mydict:
            print(nums[mydict[target-num]],nums[i],target)
            return [mydict[target-num],i]
        mydict[num] = i
        
if __name__ == "__main__":
    N = 100000 # input nums length,can be change
    tmpN = 10*N
    tmpnums = list(range(tmpN))
    random.shuffle(tmpnums)
    nums = tmpnums[:N]
    target = random.randint(0,tmpN) + N//10
    
    start = time.time()
    print(method1(nums,target))
    print("method1 use time {0:.10f} s".format(time.time()-start))
    
    start = time.time()
    print(method2(nums,target))
    print("method1 use time {0:.10f} s".format(time.time()-start))
    
    start = time.time()
    print(method3(nums,target))
    print("method1 use time {0:.10f} s".format(time.time()-start))
    