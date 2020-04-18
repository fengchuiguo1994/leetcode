import time
import random

def generate(numRows):
    if numRows == 0:
        return []
    result = [[1]]
    if numRows == 1:
        return result
    for i in range(1,numRows):
        tmp = []
        for j in range(i+1):
            if j-1 < 0:
                tmp.append(result[i-1][j])
            elif j == len(result[i-1]):
                tmp.append(result[i-1][-1])
            else:
                tmp.append(result[i-1][j-1]+result[i-1][j])
        result.append(tmp)
    return result
        
        
if __name__ == "__main__": 
    nums1 = 5
    
    start = time.time()
    print(generate(nums1))
    print("generate use time {0:.10f} s".format(time.time()-start))