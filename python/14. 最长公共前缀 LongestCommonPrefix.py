import time
import random

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    
    index = 0 # 当前长度
    flag = True
    sts = "" # 共同序列
    while flag:
        if index >= len(strs[0]):
            break
        tmp = strs[0][index]
        for i in strs:
            if index >= len(i) or i[index] != tmp:
                flag = False
                break
        if flag:
            index += 1
            sts += tmp
    return sts

if __name__ == "__main__":
    words = 'qwertyuiopasdfghjklzxcvbnm'
    prefix = ""
    suf = []
    for i in range(random.randint(0,10)):
        prefix += random.choice(words)
    for i in range(random.randint(0,10)):
        tmp = ""
        for i in range(random.randint(0,10)):
            tmp += random.choice(words)
        suf.append(tmp)
    if random.randint(0,1) == 1:
        for i in range(len(suf)):
            suf[i] = prefix+suf[i]
    print(suf)
    
    start = time.time()
    print(longestCommonPrefix(suf))
    print("longestCommonPrefix use time {0:.10f} s".format(time.time()-start))
