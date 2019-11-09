class Solution:
    def findMedianSortedArrays(self, nums1: "List[int]", nums2: "List[int]") -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        meadian = {}
        if (length1+length2)%2 == 0:
            tmp = int((length1+length2)/2)
            meadian[tmp] = None
            meadian[tmp+1] = None
        else:
            tmp = int((length1+length2)/2+1)
            meadian[tmp] = None
        n = m = 0
        total = 0
        while n < length1 and m < length2:
            if nums1[n] < nums2[m]:
                total += 1
                if total in meadian:
                    meadian[total] = nums1[n]
                n += 1
            else:
                total += 1
                if total in meadian:
                    meadian[total] = nums2[m]
                m += 1
        while n < length1:
            total += 1
            if total in meadian:
                meadian[total] = nums1[n]
            n += 1
        while m < length2:
            total += 1
            if total in meadian:
                meadian[total] = nums2[m]
            m += 1
        if len(meadian) == 1:
            return list(meadian.values())[0]
        else:
            tmp = list(meadian.values())
            return (tmp[0]+tmp[1])/2
        

aa = [1,2]
bb = [3,4]
print(Solution().findMedianSortedArrays(aa,bb))