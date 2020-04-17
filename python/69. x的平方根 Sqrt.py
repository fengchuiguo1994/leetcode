import time
import random

def mySqrt(x):
    aa = 1
    while int(aa)!=int(x/aa):
        aa = (x/aa+aa)/2
        print(aa)
    return int(aa)

if __name__ == "__main__": 
    x = 2147395599
    
    start = time.time()
    print(mySqrt(x))
    print("mySqrt use time {0:.10f} s".format(time.time()-start))