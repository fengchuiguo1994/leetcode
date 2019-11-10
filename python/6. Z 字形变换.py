class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s)<=1:
            return s
        mylist = []
        for i in range(numRows):
            mylist.append([])
            if i == 0 or i == numRows-1:
                n = 0
                while i+2*n*(numRows-1) < len(s):
                    mylist[i].append(s[i+2*n*(numRows-1)])
                    n += 1
            else:
                n = 0
                while i+2*n*(numRows-1) < len(s):
                    # print(i+2*n*(numRows-1),2*(numRows-1)-i+2*n*(numRows-1))
                    mylist[i].append(s[i+2*n*(numRows-1)])
                    try:
                        s[2*(numRows-1)-i+2*n*(numRows-1)]
                        mylist[i].append(s[2*(numRows-1)-i+2*n*(numRows-1)])
                    except IndexError:
                        pass
                    n += 1
        return "".join(["".join(x) for x in mylist])
            
aa = ""
bb = [3,4]
print(Solution().convert(aa,3))