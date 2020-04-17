import time
import random

def addBinary(a,b):
    new = ""
    aindex = len(a)-1
    bindex = len(b)-1
    maxindex = max(aindex,bindex)
    index = 0
    flag = 0
    while index<=maxindex:
        if index <= aindex and index <= bindex:
            tmp = int(a[aindex-index])+int(b[bindex-index])+flag
        elif index > aindex:
            tmp = 0+int(b[bindex-index])+flag
        else:
            tmp = int(a[aindex-index])+0+flag
        if tmp>=2:
            new = str(tmp-2)+new
            flag = 1
        else:
            new = str(tmp)+new
            flag = 0
        index += 1
    if flag == 1:
        new = '1'+new
    return new

if __name__ == "__main__": 
    a = '1010'
    b = '101'
    
    start = time.time()
    print(addBinary(a,b))
    print("addBinary use time {0:.10f} s".format(time.time()-start))