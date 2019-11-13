class Solution:    
    def intToRoman(self, num: int) -> str:
        mydict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        tmp = num%10000
        num = num//10000
        mylist = []
        mylist.append('{0}'.format('M'*(tmp//1000)))
        tmp = tmp%1000
        mylist.extend(trans(tmp,100,mydict[100],mydict[500],mydict[1000]))
        tmp = tmp%100
        mylist.extend(trans(tmp,10,mydict[10],mydict[50],mydict[100]))
        tmp = tmp%10
        mylist.extend(trans(tmp,1,mydict[1],mydict[5],mydict[10]))
        return ''.join(mylist)

def trans(tmp,times,c1,c2,c3):
    order = []
    if tmp//times < 4:
        order.append('{0}'.format(c1*(tmp//times)))
    elif tmp//times == 4:
        order.append('{0}{1}'.format(c1,c2))
    elif tmp//times == 5:
        order.append(c2)
    elif tmp//times > 5 and tmp//times < 9:
        order.append('{0}{1}'.format(c2,c1*(tmp//times-5)))
    elif tmp//times == 9:
        order.append('{0}{1}'.format(c1,c3))
    return(order)
    
aa = 58
print(Solution().intToRoman(aa))