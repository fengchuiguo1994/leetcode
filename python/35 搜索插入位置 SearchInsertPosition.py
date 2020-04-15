import time
import random

def searchInsert(nums,target):
    for i,j in enumerate(nums):
        if j < target:
            pass
        elif j==target:
            return i
        else:
            nums.insert(i,target)
            return i
    nums.append(target)
    return len(nums)-1
        
if __name__ == "__main__":
    aa = list(range(100))
    random.shuffle(aa)
    myarr = aa[:random.randint(0,10)]
    target = random.randint(0,10)
    print(myarr,target)
    
    start = time.time()
    print(searchInsert(myarr,target))
    print(myarr)
    print("searchInsert use time {0:.10f} s".format(time.time()-start))