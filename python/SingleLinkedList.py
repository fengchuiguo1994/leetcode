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
    
    def __len__(self):
        """
        获取表的长度
        """
        return self.length
    
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
    
    def reverse(self):
        """
        反转
        """
        if self.length < 2:
            pass
        else:
            pre = self.head
            current = pre.getNext()
            pnext = current.getNext()
            pre.setNext(None)
            while pnext:
                current.setNext(pre)
                pre = current
                current = pnext
                pnext = current.getNext()
            current.setNext(pre)
            self.head = current
    
    def reverseSub(self,start,end):
        """
        反转指定区域的链表
        """
        if start >= end:
            raise Exception('指定的索引start必须小于end')
        elif start > self.length-1:
            raise Exception('指定的索引start必须小于链表长度')
        elif start < 0:
            raise Exception('指定的索引start必须大于0')
        if end > self.length:
            end = self.length        
        if end - start == 1:
            pass
    
    def for_each(self,proc):
        """
        遍历
        aa.for_each(print)
        """
        current = self.head
        while current is not None:
            proc(current.getNode())
            current = current.getNext()
    
    def elements(self):
        """
        迭代器
        """
        current = self.head
        while current is not None:
            yield current.getNode()
            current = current.getNext()
            
    def filter(self,pred):
        """
        筛选生成器
        for i in aa.filter(List.even):
            print(i)
        """
        current = self.head
        while current is not None:
            if pred(current.getNode()):
                yield current.getNode()
            current = current.getNext()
    
    @staticmethod
    def even(n):
        return n%2==0
    
    def size(self):
        """
        获取表的长度
        """
        return self.length
    
    def destroy(self):
        """
        析构
        """
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
    
class LList(List):
    def __init__(self,x=[]):
        List.__init__(self,x)
        if len(x) == 0:
            self.end = None
        else:
            nodes = self.head
            while nodes.getNext():
                nodes = nodes.getNext()
            self.end = nodes
    
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
            self.end = temp
        else:
            self.end.setNext(temp)
            self.end = self.end.getNext()
        self.length += 1