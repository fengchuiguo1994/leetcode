# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def listToChaian(mylist):
    dummyRoot = ListNode(mylist[0])
    ptr = dummyRoot
    for number in mylist[1:]:
        ptr.next = ListNode(number)
        ptr = ptr.next
    return dummyRoot

def ChaianTolist(mynode):
    mylist = []
    head = mynode
    while head:
        mylist.append(head.val)
        head = head.next
    return mylist

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        xunl1 = l1
        xunl2 = l2
        mylist = []
        flag = 0
        while xunl1 or xunl2:
            if xunl1:
                val1 = xunl1.val
                xunl1 = xunl1.next
            else:
                val1 = 0
                xunl1 = xunl1
            if xunl2:
                val2 = xunl2.val
                xunl2 = xunl2.next
            else:
                val2 = 0
                xunl2 = xunl2
            if val1 + val2 + flag > 9:
                mylist.append(val1 + val2 - 10 + flag)
                flag = 1
            else:
                mylist.append(val1 + val2 + flag)
                flag = 0
        if flag == 1:
            mylist.append(1)
        return listToChaian(mylist)


aa = [2,4,3]
bb = [5,6,4]
cc = Solution().addTwoNumbers(listToChaian(aa),listToChaian(bb))
print(ChaianTolist(cc))