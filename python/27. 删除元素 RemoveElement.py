import time
import random

def removeElement(nums,val):
    mark = 0
    for i in nums:
        if i == val:
            pass
        else:
            nums[mark] = i
            mark += 1
    return mark
        
if __name__ == "__main__":
    aa = []
    for i in range(random.randint(0,10)):
        aa.append(random.randint(0,10))
    if len(aa) > 0:
        val = random.choice(aa)
    else:
        val = random.randint(0,10)
    print(aa,val)
    
    start = time.time()
    print(removeElement(aa,val))
    print(aa)
    print("removeElement use time {0:.10f} s".format(time.time()-start))