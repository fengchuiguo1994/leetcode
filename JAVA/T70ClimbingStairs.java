public class T70ClimbingStairs {
    public static int climbStairs(int n) {
        if(n==1) return 1;
        if(n==2) return 2;
        int a = 1;
        int b = 2;
        for(int i=2;i<n;i++){
            int tmp = a+b;
            a = b;
            b = tmp;
        }
        return b;
    }

    public static void main(String[] args){
        int x = 38;
        long start = System.currentTimeMillis();
        System.out.println(climbStairs(x));
        System.out.println(String.format("climbStairs use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
