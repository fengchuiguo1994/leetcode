import time
import random

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         
def array2List(n):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for x in n:
        ptr.next = ListNode(x)
        ptr = ptr.next
    return dummyRoot.next

def show(n):
    tmp = []
    while n:
        tmp.append(str(n.val))
        n = n.next
    return ",".join(tmp)
    
def deleteDuplicates(head):
    if not head:
        return head
    if not head.next:
        return head        
    pre = head
    current = head.next
    flag = head.val
    while current:
        if flag == current.val:
            pre.next = current.next
            current = pre.next
        else:
            pre = pre.next
            current = current.next
            flag = pre.val
    return head
        
if __name__ == "__main__": 
    aa = []
    aalist = array2List(aa)
    print(show(aalist))
    
    start = time.time()
    print(show(deleteDuplicates(aalist)))
    print("deleteDuplicates use time {0:.10f} s".format(time.time()-start))