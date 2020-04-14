import time
import random

from SingleLinkedList import List

def mergeTwoLists1(l1:List,l2:List)->List:
    p1 = l1.head
    p2 = l2.head
    result = List()
    while p1 and p2:
        if p1.val >= p2.val:
            result.add(p2.val)
            p2 = p2.next
        else:
            result.add(p1.val)
            p1 = p1.next
    while p1:
        result.add(p1.val)
        p1 = p1.next
    while p2:
        result.add(p2.val)
        p2 = p2.next
    return result

def mergeTwoLists2(l1:ListNode,l2:ListNode)->ListNode:
    # for LeetCode
    p1 = l1
    p2 = l2
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    while p1 and p2:
        if p1.val >= p2.val:
            ptr.next = ListNode(p2.val)
            ptr = ptr.next
            p2 = p2.next
        else:
            ptr.next = ListNode(p1.val)
            ptr = ptr.next
            p1 = p1.next
    while p1:
        ptr.next = ListNode(p1.val)
        ptr = ptr.next
        p1 = p1.next
    while p2:
        ptr.next = ListNode(p2.val)
        ptr = ptr.next
        p2 = p2.next
    ptr = dummyRoot.next
    return ptr
    
    
if __name__ == "__main__":
    aatmp = []
    bbtmp = []
    for i in range(random.randint(0,10)):
        aatmp.append(random.randint(0,10))
    for i in range(random.randint(0,10)):
        bbtmp.append(random.randint(0,10))
    aatmp.sort()
    bbtmp.sort()
    aa = List(aatmp)
    bb = List(bbtmp)
    print(aa)
    print(bb)
    
    start = time.time()
    print(mergeTwoLists1(aa,bb))
    print("mergeTwoLists use time {0:.10f} s".format(time.time()-start))