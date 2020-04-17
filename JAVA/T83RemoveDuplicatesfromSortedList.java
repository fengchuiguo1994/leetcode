import List.ListNode;

public class T83RemoveDuplicatesfromSortedList {
    public static ListNode array2list(int[] x){
        ListNode dummyRoot = new ListNode(0);
        ListNode ptr = dummyRoot;
        for(int a:x){
            ptr.next = new ListNode(a);
            ptr = ptr.next;
        }
        return dummyRoot.next;
    }

    public static String show(ListNode head){
        StringBuilder tmp = new StringBuilder();
        ListNode ptr = head;
        while(ptr!=null){
            tmp.append(ptr.val);
            ptr = ptr.next;
        }
        return tmp.toString();
    }

    public static ListNode deleteDuplicates(ListNode head) {
        if(head==null || head.next == null){ // 没有或者只有一个节点
            return head;
        }
        ListNode pre = head;
        ListNode current = pre.next;
        int flag = head.val;
        while(current!=null){
            if(flag == current.val){
                pre.next = current.next;
                current = pre.next;
            } else {
                pre = pre.next;
                current = current.next;
                flag = pre.val;
            }
        }
        return head;
    }

    public static void main(String[] args){
        int[] x = {1,1,2,3,3};
        ListNode xlist = array2list(x);
        System.out.println(show(xlist));

        long start = System.currentTimeMillis();
        deleteDuplicates(xlist);
        System.out.println(show(xlist));
        System.out.println(String.format("deleteDuplicates use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
