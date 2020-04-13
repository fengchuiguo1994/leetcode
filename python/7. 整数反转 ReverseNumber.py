import time
import random

def mod(a,n):
    return a-n*int(a/n)
    # return a-n*int(a/n) # python 自带的取模方式

def rem(a,n):
    return int(a/n)
    # return a//n # python 自带的取余方式
    
def method1(x):
    if x < -int(2**31-1) or x > int(2**31-1):
        return 0
    if x < 0:
        x = abs(x)
        tmp = int("-"+str(x)[::-1])
    else:
        tmp = int(str(x)[::-1])
    if tmp < -int(2**31-1) or tmp > int(2**31-1):
        return 0
    else:
        return tmp
    
def method2(x):
    rs = 0
    intMax = 2**31-1
    intMin = -2**31
    if x>intMax or x<intMin:
        return 0
    while(x!=0):
        rs = 10*rs+mod(x,10)
        x = rem(x,10)
    if rs>intMax or rs<intMin:
        return 0
    return rs
    
if __name__ == "__main__":
    N = random.randint(-2**32,2**32)
    print(N)
    
    start = time.time()
    print(method1(N))
    print("method1 use time {0:.10f} s".format(time.time()-start))
    
    start = time.time()
    print(method2(N))
    print("method1 use time {0:.10f} s".format(time.time()-start))