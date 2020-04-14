import time
import random

def isValid(s):
    if len(s)%2 != 0:
        return False
    instack = {r'(':1,r'[':2,r'{':3}
    outstack = {r')':1,r']':2,r'}':3}
    tmp = []
    for i in range(len(s)):
        if s[i] in instack:
            tmp.append(s[i])
        else:
            if(len(tmp)==0):
                return False
            bb = tmp.pop()
            if instack[bb] != outstack[s[i]]:
                return False
    if(len(tmp)==0):
        return True
    else:
        return False
        
    
if __name__ == "__main__":
    words = r'(){}[]'
    mystr = ""
    for i in range(random.randint(0,10)):
        mystr += random.choice(words)
    print(mystr)
    
    start = time.time()
    print(isValid(mystr))
    print("isValid use time {0:.10f} s".format(time.time()-start))