import java.util.Arrays;
import java.util.Random;

class ListNode{
    int val;
    ListNode next;

    ListNode(int x){
        val = x;
    }
}

public class T21MergeTwoSortedLists {
    public static ListNode array2list(int[] a){
        ListNode dummyRoot = new ListNode(0);
        ListNode ptr = dummyRoot;
        for(int x:a){
            ptr.next = new ListNode(x);
            ptr = ptr.next;
        }
        return dummyRoot.next;
    }

    public static ListNode mergeTwoLists(ListNode l1, ListNode l2){
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode dummyRoot = new ListNode(0);
        ListNode ptr = dummyRoot;
        while(p1!=null && p2!=null) {
            if (p1.val >= p2.val) {
                ptr.next = new ListNode(p2.val);
                ptr = ptr.next;
                p2 = p2.next;
            } else {
                ptr.next = new ListNode(p1.val);
                ptr = ptr.next;
                p1 = p1.next;
            }
        }
        while(p1!=null) {
            ptr.next = new ListNode(p1.val);
            ptr = ptr.next;
            p1 = p1.next;
        }
        while(p2!=null) {
            ptr.next = new ListNode(p2.val);
            ptr = ptr.next;
            p2 = p2.next;
        }
        return dummyRoot.next;
    }

    public static void main(String[] args){
        Random r = new Random();
        int tmpr = r.nextInt(10);
        int[] aa = new int[tmpr];
        for(int i=0;i<tmpr;i++){
            aa[i] = r.nextInt(10);
        }
        tmpr = r.nextInt(10);
        int[] bb = new int[tmpr];
        for(int i=0;i<tmpr;i++){
            bb[i] = r.nextInt(10);
        }
        Arrays.sort(aa);
        Arrays.sort(bb);
        ListNode listaa = array2list(aa);
        ListNode listbb = array2list(bb);

        long start = System.currentTimeMillis();
        System.out.println(mergeTwoLists(listaa,listbb));
        System.out.println(String.format("mergeTwoLists use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
