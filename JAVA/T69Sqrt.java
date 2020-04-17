public class T69Sqrt {
    public static int mySqrt(int x) {
        double a = 1;
        while((int)a != (int)(x/a)){
            a = (x/a+a)/2;
        }
        return (int)a;
    }

    public static void main(String[] args){
        int x = 2147395599;
        long start = System.currentTimeMillis();
        System.out.println(mySqrt(x));
        System.out.println(String.format("mySqrt use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
