import time
import random

def countAndSay(n):
    k = '1'
    if n==1:
        return k
    for i in range(1,n):
        flag = k[0]
        count = 1
        newstr = ''
        for j in range(1,len(k)):
            if flag != k[j]:
                newstr += str(count)
                newstr += str(flag)
                count = 0
            flag = k[j]
            count += 1
        newstr += str(count)
        newstr += str(flag)
        k = newstr
    return k

if __name__ == "__main__":    
    start = time.time()
    print(countAndSay(random.randint(1,30)))
    print("searchInsert use time {0:.10f} s".format(time.time()-start))