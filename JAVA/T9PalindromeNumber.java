import java.sql.SQLSyntaxErrorException;
import java.util.Random;

public class T9PalindromeNumber {
    public static Boolean method1(int x){
        if(x < 0){
            return Boolean.FALSE;
        }
        String str = String.valueOf(x);
        char[] chararr = str.toCharArray();
        for(int i=0;i<chararr.length/2;i++){
            if(chararr[i]!=chararr[chararr.length-1-i]){
                return Boolean.FALSE;
            }
        }
        return Boolean.TRUE;
    }

    public static Boolean method2(int x){
        if(x < 0){
            return Boolean.FALSE;
        }
        int rs = 0;
        int tmp = x;
        while(x != 0){
            rs = 10*rs+x%10;
            x = x/10;
        }
        return tmp == rs;
    }

    public static void main(String[] args){
        int N = new Random().nextInt();
        System.out.println(N);

        long start = System.currentTimeMillis();
        System.out.println(method1(N));
        System.out.println(String.format("method1 use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));

        start = System.currentTimeMillis();
        System.out.println(method2(N));
        System.out.println(String.format("method1 use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));

    }
}
