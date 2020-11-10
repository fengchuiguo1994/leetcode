import time
import random

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
def StringToTreeNode(nn):
    nn = nn.strip()
    if len(nn) == 0:
        return None
    mylist = nn.split(",")
    root = TreeNode(int(mylist[0])) # 根节点
    rootlist = [root] # 用来存放根节点的列表
    currentroot = 0 # 当前调用的根节点的索引
    index = 1 # 输入数据的索引
    while index < len(mylist):
        node = rootlist[currentroot]
        currentroot += 1
        item = mylist[index]
        index = index+1
        if item!="null":
            node.left = TreeNode(int(item))
            rootlist.append(node.left)
        if index >= len(mylist):
            break
        item = mylist[index]
        index += 1
        if item!="null":
            node.right = TreeNode(int(item))
            rootlist.append(node.right)
    return root

def show(root):
    if not root:
        return ""
    rootlist = [root]
    currentroot = 0
    result = ""
    while currentroot < len(rootlist):
        if rootlist[currentroot].val:
            result += str(rootlist[currentroot].val)
            result += "\t"
        
        if rootlist[currentroot].left:
            rootlist.append(rootlist[currentroot].left)
        if rootlist[currentroot].right:
            rootlist.append(rootlist[currentroot].right)
        currentroot += 1
    return result
    
    
def isSameTree(p,q):
    if (not p and q) or (p and not q):
        return False
    if (not p) and (not q):
        return True
    prootlist = [p]
    qrootlist = [q]
    currentroot = 0
    while currentroot < len(prootlist) and currentroot < len(qrootlist):
        if prootlist[currentroot].val != qrootlist[currentroot].val:
            return False
        
        if prootlist[currentroot].left and qrootlist[currentroot].left:
            prootlist.append(prootlist[currentroot].left)
            qrootlist.append(qrootlist[currentroot].left)
        elif (not prootlist[currentroot].left) and (not qrootlist[currentroot].left):
            pass
        else:
            return False
        if prootlist[currentroot].right and qrootlist[currentroot].right:
            prootlist.append(prootlist[currentroot].right)
            qrootlist.append(qrootlist[currentroot].right)
        elif (not prootlist[currentroot].right) and (not qrootlist[currentroot].right):
            pass
        else:
            return False
        currentroot += 1
    if len(prootlist) != len(qrootlist):
        return False
    return True

def isSymmetric(root):
    def ismirror(p,q):
        if (not p) and (not q):
            return True
        elif ((not p) and q) or (p and (not q)):
            return False
        elif p.val == q.val:
            return ismirror(p.left,q.right) and ismirror(p.right,q.left)
        else:
            return False
        
    if not root:
        return True
    return ismirror(root.left,root.right)

def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left),maxDepth(root.right))+1
    # return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
    
if __name__ == "__main__": 
    aa = "1,2"
    aatree = StringToTreeNode(aa)
    # print(show(aatree))
    bb = "1,2,2,3,4,4,3"
    bbtree = StringToTreeNode(bb)
    # print(show(bbtree))
    print(maxDepth(bbtree))
    start = time.time()
    print(isSameTree(aatree,bbtree))
    print(isSymmetric(bbtree))
    print("isSameTree use time {0:.10f} s".format(time.time()-start))