import time
import random

def removeDuplicates(nums):
    if len(nums) < 1:
        return len(nums)
    flag = nums[0]
    mark = 1
    for i in nums[1:]:
        if flag != i:
            nums[mark] = i
            flag = i
            mark += 1
    return mark
        
if __name__ == "__main__":
    aa = []
    for i in range(random.randint(0,10)):
        aa.append(random.randint(0,10))
    aa.sort()
    print(aa)
    
    start = time.time()
    print(removeDuplicates(aa))
    print(aa)
    print("removeDuplicates use time {0:.10f} s".format(time.time()-start))