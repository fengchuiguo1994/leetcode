import time
import random

def lengthOfLastWord(s:str):
    if s.strip()=="":
        return 0
    return len(s.split()[-1])

if __name__ == "__main__": 
    s = "Hello World"
    s = " "
    
    start = time.time()
    print(lengthOfLastWord(s))
    print("lengthOfLastWord use time {0:.10f} s".format(time.time()-start))