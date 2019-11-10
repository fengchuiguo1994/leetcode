class Solution:
    def reverse(self, x: int) -> int:
        if x < -int(2**31-1) or x > int(2**31-1):
            return 0
        if x < 0:
            x = abs(x)
            tmp = int("-"+"".join(reversed(list(str(x)))))
        else:
            tmp = int("".join(reversed(list(str(x)))))
        if tmp < -int(2**31-1) or tmp > int(2**31-1):
            return 0
        else:
            return tmp
            
aa = 120
bb = [3,4]
print(Solution().reverse(aa))

# int reverse(int x)
# {
#     int max = 0x7fffffff, min = 0x80000000;//int的最大值最小值
#     long rs = 0;//用long类型判断溢出
#     for(;x;rs = rs*10+x%10,x/=10);//逆序，正负通吃，不用单独考虑负值
#     return rs>max||rs<min?0:rs;//超了最大值低于最小值就返回0
# }