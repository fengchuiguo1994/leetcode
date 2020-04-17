import time
import random

def plusOne(digits):
    maxdig = len(digits)-1
    add = [1]
    maxadd = len(add)-1
    new = []
    flag = 0
    for i in range(len(digits)):
        if i > maxadd:
            if digits[maxdig-i]+0+flag >= 10:
                new.append(digits[maxdig-i]+0+flag-10)
                flag = 1
            else:
                new.append(digits[maxdig-i]+0+flag)
                flag = 0
        else:
            if digits[maxdig-i]+add[maxadd-i]+flag >= 10:
                new.append(digits[maxdig-i]+add[maxadd-i]+flag-10)
                flag = 1
            else:
                new.append(digits[maxdig-i]+add[maxadd-i]+flag)
                flag = 0
    if flag == 1:
        new.append(1)
    new.reverse()
    return new

if __name__ == "__main__": 
    s = [9,9,9]
    
    start = time.time()
    print(plusOne(s))
    print("plusOne use time {0:.10f} s".format(time.time()-start))