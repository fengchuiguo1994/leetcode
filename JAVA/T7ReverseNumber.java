import java.util.*;

public class T7ReverseNumber {

    public static int method1(int x){
        long tmpx = (long)x;
        long tmp;
        StringBuilder tmpstr = new StringBuilder();
        if(tmpx < 0){
            tmpx = Math.abs(tmpx);
            // System.out.println(Math.abs(-2147483647)); ok
            // System.out.println(Math.abs(-2147483648)); error
            tmpstr.append(tmpx).reverse();
            tmpstr.insert(0,"-");
            tmp = Long.parseLong(tmpstr.toString());
        } else {
            tmpstr.append(tmpx).reverse();
            tmp = Long.parseLong(tmpstr.toString());
        }
        if(tmp>Integer.MAX_VALUE || tmp<Integer.MIN_VALUE){
            return 0;
        }
        return (int)tmp;
    }

    public static int method2(int x){
        long rs = 0;
        while(x != 0){
            rs = 10*rs+x%10;
            x = x/10;
        }
        if(rs>Integer.MAX_VALUE || rs<Integer.MIN_VALUE){
            return 0;
        }
        return (int)rs;
    }
    public static void main(String[] args){
        int N = new Random().nextInt();
        // N = -2147483648;
        System.out.println(N);
        long start = System.currentTimeMillis();
        System.out.println(method1(N));
        System.out.println(String.format("method1 use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));

        start = System.currentTimeMillis();
        System.out.println(method2(N));
        System.out.println(String.format("method1 use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));

    }
}
