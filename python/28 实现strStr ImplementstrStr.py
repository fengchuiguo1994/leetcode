import time
import random

def strStr(haystack,needle):
    if len(needle) == 0:
        return 0
    length = len(needle)
    for i in range(0,len(haystack)-length+1):
        if haystack[i:i+length] == needle:
            return i
    return -1
    
        
if __name__ == "__main__":
    words = "qwertyuiopasdfghjklzxcvbnm"
    words += words.upper()
    mystr = ""
    target = ""
    for i in range(random.randint(1,10)):
        mystr += random.choice(words)
    if random.randint(0,1) == 1:
        target = mystr[random.randint(0,len(str)//2):random.randint(len(str)//2,len(str))]
    else:
        for i in range(random.randint(0,10)):
            target += random.choice(words)
    print(mystr,target)
    
    start = time.time()
    print(strStr(mystr,target))
    print("strStr use time {0:.10f} s".format(time.time()-start))