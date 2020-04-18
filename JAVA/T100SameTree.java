import Tree.TreeNode;

import java.util.LinkedList;
import java.util.Queue;

public class T100SameTree {
    public static TreeNode string2tree(String x){
        x = x.trim();
        if(x.length()==0){
            return null;
        }
        String[] tmp = x.split(",");
        String item = tmp[0];
        item.trim();
        TreeNode root = new TreeNode((Integer.parseInt(item)));
        Queue<TreeNode> rootqueue = new LinkedList<>();
        rootqueue.add(root);
        int index = 1;
        while(!rootqueue.isEmpty()){
            TreeNode node = rootqueue.remove();
            if(index == tmp.length){
                break;
            }
            item = tmp[index].trim();
            if(!item.equals("null")){
                node.left = new TreeNode(Integer.parseInt(item));
                rootqueue.add(node.left);
            }
            index++;
            if(index == tmp.length){
                break;
            }
            item = tmp[index].trim();
            if(!item.equals("null")){
                node.right = new TreeNode(Integer.parseInt(item));
                rootqueue.add(node.right);
            }
            index++;
        }
        return root;
    }

    public static void show(TreeNode root,StringBuilder result){
        if(root != null){
            result.append(root.val);
            show(root.left,result);
            show(root.right,result);
        }
    }

    public static void show2(TreeNode root,StringBuilder result){
        if(root != null){
            show(root.left,result);
            result.append(root.val);
            show(root.right,result);
        }
    }

    public static void show3(TreeNode root,StringBuilder result){
        if(root != null){
            show(root.left,result);
            show(root.right,result);
            result.append(root.val);
        }
    }

    public static boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null){
            return true;
        } else if(p != null && q != null){
            return p.val == q.val && isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
        } else {
            return false;
        }
    }

    public static boolean isSymmetric(TreeNode root) {
        if(root == null){ // 没有节点
            return true;
        }  else {
            return ismirror(root.left,root.right);
        }
    }

    public static boolean ismirror(TreeNode p, TreeNode q) {
        if(p == null && q == null ){
            return true;
        } else if(p == null && q != null ){
            return false;
        } else if(p != null && q == null ) { // 一个根节点加左节点
            return false;
        } else if(p.val == q.val){
            return ismirror(p.left,q.right) && ismirror(p.right,q.left);
        } else {
            return false;
        }
    }

    public static int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }
        return Math.max(maxDepth(root.left),maxDepth(root.right))+1;
    }

    public static void main(String[] args){
        String aa = "1,2,3";
        String bb = "1,2,2,3,3";
        StringBuilder aresult = new StringBuilder();
        StringBuilder bresult = new StringBuilder();
        TreeNode aatree = string2tree(aa);
        TreeNode bbtree = string2tree(bb);
        show3(bbtree,bresult);
        System.out.println(bresult.toString());
        System.out.println(isSymmetric(bbtree));
        System.out.println(maxDepth(bbtree));

        long start = System.currentTimeMillis();
        System.out.println(isSameTree(aatree,bbtree));
        System.out.println(String.format("isSameTree use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
