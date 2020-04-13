import time
import random

def method1(x):
    if x < 0:
        return False
    aa = str(x)
    length = len(aa)
    for i in range(length//2):
        if aa[i] != aa[length-i-1]:
            return False
    return True

def method2(x):
    if x < 0:
        return False
    aa = str(x)
    return aa == aa[::1]
            
if __name__ == "__main__":
    N = random.randint(-2**32,2**32)
    N = 10
    print(N)
    
    start = time.time()
    print(method1(N))
    print("method1 use time {0:.10f} s".format(time.time()-start))
    
    start = time.time()
    print(method2(N))
    print("method1 use time {0:.10f} s".format(time.time()-start))