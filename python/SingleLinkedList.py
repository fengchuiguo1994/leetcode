import sys

class ListNode:
    def __init__(self,x,pnext=None):
        self.val = x
        self.next = pnext
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return self.__str__()
    def getNode(self):
        return self.val
    def getNext(self):
        return self.next
    def setNext(self,newNode):
        self.next = newNode
        
class List:
    def __init__(self,x=[]):
        """
        初始化
        """
        self.head = None
        self.length = 0
        if len(x)>0:
            for i in x:
                self.add(i)
    
    def isEmpty(self):
        """
        是否为空
        """
        return self.length == 0
    
    def add(self,data):
        """
        添加元素
        """
        if not isinstance(data,ListNode):
            temp = ListNode(data)
        else:
            temp = data
        if self.isEmpty():
            self.head = temp
            self.length += 1
        else:
            p = self.head
            while p.getNext():
                p = p.getNext()
            p.setNext(temp)
            self.length += 1
    
    def pop(self):
        """
        移除最后的元素
        """
        if self.isEmpty():
            # 当列表为空的时候，直接抛出
            sys.exit("The ListNode is empty")
        elif self.length == 1:
            # 第一个节点就是要移除的，此时链表为空
            temp = self.head.val
            self.head = None
            self.length -= 1
        else:
            p = self.head
            pnext = p.getNext()
            while pnext.getNext():
                p = p.getNext()
                pnext = pnext.getNext()
            temp = pnext.val
            p.setNext(None)
            self.length -= 1
        return temp
        
    
    def search(self,data):
        """
        寻找指定元素
        """
        if isinstance(data,ListNode):
            temp = data.val
        else:
            temp = data
        p = self.head
        while p:
            if p.val == temp:
                return True
            p = p.getNext()
        return False
    
    def index(self,data):
        """
        指定元素索引
        """
        if isinstance(data,ListNode):
            temp = data.val
        else:
            temp = data
        index = 0
        p = self.head
        while p:
            if p.val == temp:
                return index
            index += 1
            p = p.getNext();
        return -1
    
    def remove(self,data):
        """
        移除指定元素
        """
        if self.isEmpty():
            return 0
        if isinstance(data,ListNode):
            temp = data.val
        else:
            temp = data
        p = self.head
        if p.val == temp:
            # 当head就要删除的时候，只需要将head指向下个节点就行
            self.head = p.getNext()
            self.length -= 1
            return 1
        else:
            # 当不是第一个的时候，需要另一个变量来记录下一个node，然后判断下一个node是否移除
            pnext = p.getNext()
            while pnext:
                if pnext.val == temp:
                    p.setNext(pnext.getNext())
                    self.length -= 1
                    return 1
                p = p.getNext()
                pnext = pnext.getNext()
        return 0
    
    def insert(self,pos,data):
        """
        插入元素
        """
        if not isinstance(data,ListNode):
            temp = ListNode(data)
        else:
            temp = data
        if pos >= self.length:
            # 此时插入元素超过了最大索引，所以默认放最后
            self.add(temp)
        elif pos == 0:
            # 插入到第一位，需要修改head
            p = self.head
            self.head = temp
            self.head.setNext(p)
            self.length += 1
        else:
            # 插入中间某个位置
            p = self.head
            pnext = p.getNext()
            count = 1
            while pnext:
                if count == pos:
                    p.setNext(temp)
                    p.getNext().setNext(pnext)
                    self.length += 1
                    break
                p = p.getNext()
                pnext = pnext.getNext()
                count += 1
    
    def size(self):
        return self.length
    
    def destroy(self):
        self.head = None
        self.length = 0
            
    def __repr__(self):
        if self.length == 0:
            return "[]"
        result = ""
        p = self.head
        while p:
            result += str(p.val)+","
            p = p.getNext()
        return "["+result[:-1]+"]"
    
    def __str__(self):
        return self.__repr__()