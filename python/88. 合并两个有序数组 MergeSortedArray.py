import time
import random

def merge(nums1,m,nums2,n):
    index = m+n-1
    while m>0 and n>0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[index] = nums1[m-1]
            m = m-1
        else:
            nums1[index] = nums2[n-1]
            n = n-1
        index -= 1
    if n>0:
        for t in range(0,n):
            nums1[t] = nums2[t]
        
if __name__ == "__main__": 
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    
    start = time.time()
    merge(nums1,m,nums2,n)
    print(nums1)
    print("merge use time {0:.10f} s".format(time.time()-start))