import time
import random

def intToRoman(num):
    mydict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
    mylist = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    s = ""
    while(num>0):
        for aa in mylist:
            if num>=aa:
                s += mydict[aa]
                num -= aa
                break
    return s

def romanToInt(s):
    mydict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    total = 0
    index = 0
    while(index < len(s)):
        if index == len(s)-1 or mydict[s[index]] >= mydict[s[index+1]]:
            total += mydict[s[index]]
        else:
            total += mydict[s[index:index+2]]
            index += 1
        index += 1
    return total

if __name__ == "__main__":
    N = random.randint(0,10000)
    print(N)
    
    start = time.time()
    aa = intToRoman(N)
    print(aa) 
    print("intToRoman use time {0:.10f} s".format(time.time()-start))
    
    start = time.time()
    print(romanToInt(aa))
    print("romanToInt use time {0:.10f} s".format(time.time()-start))
    